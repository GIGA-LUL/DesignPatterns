class Bytecode:
    def __init__(self, code):
        self.code = code


class BytecodeStream:
    def __init__(self):
        self.bytecode_list = []

    def add_bytecode(self, bytecode):
        self.bytecode_list.append(bytecode)

    def get_bytecode(self):
        return self.bytecode_list


class Token:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Token({self.value})"


class Scanner:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def scan(self):
        tokens = []
        for char in self.input_stream:
            if char.strip():
                tokens.append(Token(char))
        return tokens


class ProgramNode:
    def __init__(self):
        self.children = []

    def add(self, node):
        self.children.append(node)

    def traverse(self, code_generator):
        code_generator.visit_statement(self)
        for child in self.children:
            child.traverse(code_generator)


class VariableNode(ProgramNode):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def traverse(self, code_generator):
        code_generator.visit_expression(self)

    def __repr__(self):
        return f"Variable({self.name})"


class AssignmentNode(ProgramNode):
    def __init__(self, variable, expression):
        super().__init__()
        self.variable = variable
        self.expression = expression
        self.add(variable)
        self.add(expression)

    def traverse(self, code_generator):
        code_generator.visit_statement(self)
        self.variable.traverse(code_generator)
        self.expression.traverse(code_generator)

    def __repr__(self):
        return f"Assignment({self.variable} = {self.expression})"


class ExpressionNode(ProgramNode):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def traverse(self, code_generator):
        code_generator.visit_expression(self)

    def __repr__(self):
        return f"Expression({self.value})"


class ProgramNodeBuilder:
    def __init__(self):
        self._node = ProgramNode()

    def new_variable(self, variable_name):
        return VariableNode(variable_name)

    def new_assignment(self, variable, expression):
        return AssignmentNode(variable, expression)

    def new_expression(self, value):
        return ExpressionNode(value)

    def get_root_node(self):
        return self._node


class Parser:
    def __init__(self):
        pass

    def parse(self, scanner, builder):
        tokens = list(scanner.scan())
        variable = builder.new_variable(tokens[0].value)
        expression = builder.new_expression(tokens[4].value)
        assignment = builder.new_assignment(variable, expression)
        builder.get_root_node().add(assignment)


class CodeGenerator:
    def __init__(self, output_stream):
        self._output = output_stream

    def visit_statement(self, node):
        raise NotImplementedError

    def visit_expression(self, node):
        raise NotImplementedError


class RISCCodeGenerator(CodeGenerator):
    def visit_statement(self, node):
        bytecode = Bytecode(f"RISC_CODE_FOR_STATEMENT {node}")
        self._output.add_bytecode(bytecode)

    def visit_expression(self, node):
        bytecode = Bytecode(f"RISC_CODE_FOR_EXPRESSION {node}")
        self._output.add_bytecode(bytecode)


class Compiler:
    def __init__(self):
        pass

    def compile(self, input_stream, output_stream):
        scanner = Scanner(input_stream)
        builder = ProgramNodeBuilder()
        parser = Parser()
        parser.parse(scanner, builder)

        generator = RISCCodeGenerator(output_stream)
        parse_tree = builder.get_root_node()
        parse_tree.traverse(generator)


if __name__ == "__main__":
    input_program = "x = 1 + 2"
    input_stream = iter(input_program)
    output_stream = BytecodeStream()

    compiler = Compiler()
    compiler.compile(input_stream, output_stream)

    for bytecode in output_stream.get_bytecode():
        print(bytecode.code)
