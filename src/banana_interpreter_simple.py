#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Banana 语言解释器
简化版解释器，支持基本语法和功能
"""

import re
import math
import random
from datetime import datetime

# 词法分析器（Lexer）
class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.tokens = []
        self.keywords = {
            'banana': 'BANANA',
            'end': 'END',
            'print': 'PRINT',
            'println': 'PRINTLN',
            'input': 'INPUT',
            'input_num': 'INPUT_NUM',
            'let': 'LET',
            'set': 'SET',
            'if': 'IF',
            'else': 'ELSE',
            'endif': 'ENDIF',
            'while': 'WHILE',
            'endwhile': 'ENDWHILE',
            'for': 'FOR',
            'endfor': 'ENDFOR',
            'in': 'IN',
            'func': 'FUNC',
            'endfunc': 'ENDFUNC',
            'return': 'RETURN',
            'import': 'IMPORT',
            'str': 'STR',
            'int': 'INT',
            'float': 'FLOAT',
            'list': 'LIST',
            'len': 'LEN',
            'max': 'MAX',
            'min': 'MIN',
            'sum': 'SUM',
        'rand': 'RAND',
        'import': 'IMPORT',
        'from': 'FROM',
        'as': 'AS',
        'None': 'NONE',
        'True': 'TRUE',
        'False': 'FALSE'
        }
    
    def tokenize(self):
        while self.pos < len(self.code):
            char = self.code[self.pos]
            
            # 跳过空白字符
            if char.isspace():
                self.pos += 1
            # 处理/#include指令
            elif char == '#' and self.pos + 1 < len(self.code) and self.code[self.pos + 1] == '/':
                self.pos += 2  # 跳过/#
                # 跳过空格
                while self.pos < len(self.code) and self.code[self.pos].isspace():
                    self.pos += 1
                # 读取include的文件路径
                start = self.pos
                while self.pos < len(self.code) and self.code[self.pos] != '\n':
                    self.pos += 1
                include_path = self.code[start:self.pos].strip()
                # 移除引号
                if include_path.startswith('"') and include_path.endswith('"'):
                    include_path = include_path[1:-1]
                elif include_path.startswith('\'') and include_path.endswith('\''):
                    include_path = include_path[1:-1]
                # 处理文件包含
                self._process_include(include_path)
            # 处理注释
            elif char == '#':
                while self.pos < len(self.code) and self.code[self.pos] != '\n':
                    self.pos += 1
            # 处理字符串
            elif char == '"':
                self.pos += 1
                start = self.pos
                while self.pos < len(self.code) and self.code[self.pos] != '"':
                    self.pos += 1
                string = self.code[start:self.pos]
                self.tokens.append(('STRING', string))
                self.pos += 1
            # 处理数字
            elif char.isdigit():
                start = self.pos
                has_dot = False
                while self.pos < len(self.code) and (self.code[self.pos].isdigit() or self.code[self.pos] == '.'):
                    if self.code[self.pos] == '.':
                        if has_dot:
                            break  # 只允许一个小数点
                        has_dot = True
                    self.pos += 1
                number = self.code[start:self.pos]
                if '.' in number:
                    self.tokens.append(('NUMBER', float(number)))
                else:
                    self.tokens.append(('NUMBER', int(number)))
            elif char == '.':
                # 单独的点号作为其他字符处理
                self.pos += 1
            # 处理标识符和关键字
            elif char.isalpha() or char == '_':
                start = self.pos
                while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == '_'):
                    self.pos += 1
                identifier = self.code[start:self.pos]
                if identifier in self.keywords:
                    self.tokens.append((self.keywords[identifier], identifier))
                else:
                    self.tokens.append(('ID', identifier))
            # 处理操作符和标点
            elif char == '+':
                self.tokens.append(('ADD', '+'))
                self.pos += 1
            elif char == '-':
                self.tokens.append(('SUB', '-'))
                self.pos += 1
            elif char == '*':
                self.tokens.append(('MUL', '*'))
                self.pos += 1
            elif char == '/':
                self.tokens.append(('DIV', '/'))
                self.pos += 1
            elif char == '%':
                self.tokens.append(('MOD', '%'))
                self.pos += 1
            elif char == '^':
                self.tokens.append(('POW', '^'))
                self.pos += 1
            elif char == '=':
                self.tokens.append(('EQ', '='))
                self.pos += 1
            elif char == '>':
                self.tokens.append(('GT', '>'))
                self.pos += 1
            elif char == '<':
                self.tokens.append(('LT', '<'))
                self.pos += 1
            elif char == '(':
                self.tokens.append(('LPAREN', '('))
                self.pos += 1
            elif char == ')':
                self.tokens.append(('RPAREN', ')'))
                self.pos += 1
            elif char == '[':
                self.tokens.append(('LBRACKET', '['))
                self.pos += 1
            elif char == ']':
                self.tokens.append(('RBRACKET', ']'))
                self.pos += 1
            elif char == ',':
                self.tokens.append(('COMMA', ','))
                self.pos += 1
            else:
                # 忽略未知字符
                self.pos += 1
        return self.tokens
    
    def _process_include(self, include_path):
        """处理文件包含"""
        import os
        # 尝试不同的文件路径
        possible_paths = [
            include_path,
            f"mode/{include_path}",
            f"mode/{include_path}.BMDe",
            f"mode/{include_path}.bmde"
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        include_code = f.read()
                    # 递归处理包含的文件
                    include_lexer = Lexer(include_code)
                    include_tokens = include_lexer.tokenize()
                    # 将包含的文件的tokens添加到当前tokens中
                    self.tokens.extend(include_tokens)
                    print(f"✓ 成功包含文件: {path}")
                except Exception as e:
                    print(f"Error: 包含文件 {path} 失败: {e}")
                return
        
        print(f"Error: 包含文件 {include_path} 未找到")

# 语法分析器和执行引擎
class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.token_pos = 0
        self.tokens = []
    
    def parse(self, tokens):
        self.tokens = tokens
        self.token_pos = 0
        self._parse_program()
    
    def _parse_program(self):
        # 解析程序开始
        self._expect('BANANA')
        # 解析语句列表
        while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'END':
            self._parse_statement()
        # 解析程序结束
        self._expect('END')
    
    def _parse_statement(self):
        token_type, token_value = self.tokens[self.token_pos]
        
        if token_type == 'PRINT':
            self.token_pos += 1
            self._expect('LPAREN')
            value = self._parse_expression()
            self._expect('RPAREN')
            print(str(value), end='')
        
        elif token_type == 'PRINTLN':
            self.token_pos += 1
            self._expect('LPAREN')
            value = self._parse_expression()
            self._expect('RPAREN')
            print(str(value))
        
        elif token_type == 'INPUT':
            self.token_pos += 1
            self._expect('LPAREN')
            prompt = self._parse_expression()
            self._expect('RPAREN')
            value = input(str(prompt))
            self._expect('LET')
            var_name = self._expect('ID')[1]
            self._expect('EQ')
            self.variables[var_name] = value
        
        elif token_type == 'INPUT_NUM':
            self.token_pos += 1
            self._expect('LPAREN')
            prompt = self._parse_expression()
            self._expect('RPAREN')
            value = float(input(str(prompt)))
            self._expect('LET')
            var_name = self._expect('ID')[1]
            self._expect('EQ')
            self.variables[var_name] = value
        
        elif token_type == 'LET':
            self.token_pos += 1
            var_name = self._expect('ID')[1]
            self._expect('EQ')
            value = self._parse_expression()
            self.variables[var_name] = value
        
        elif token_type == 'SET':
            self.token_pos += 1
            var_name = self._expect('ID')[1]
            self._expect('EQ')
            value = self._parse_expression()
            if var_name in self.variables:
                self.variables[var_name] = value
            else:
                print(f"Error: Variable {var_name} not defined")
        
        elif token_type == 'IF':
            self.token_pos += 1
            condition = self._parse_expression()
            if condition:
                while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'ELSE' and self.tokens[self.token_pos][0] != 'ENDIF':
                    self._parse_statement()
                if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == 'ELSE':
                    # 跳过else分支
                    self.token_pos += 1
                    while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'ENDIF':
                        self.token_pos += 1
            else:
                # 跳过if分支
                while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'ELSE' and self.tokens[self.token_pos][0] != 'ENDIF':
                    self.token_pos += 1
                if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == 'ELSE':
                    self.token_pos += 1
                    while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'ENDIF':
                        self._parse_statement()
            self._expect('ENDIF')
        
        elif token_type == 'WHILE':
            self.token_pos += 1
            start_pos = self.token_pos - 1
            condition = self._parse_expression()
            while condition:
                self.token_pos = start_pos + 1
                condition = self._parse_expression()
                if not condition:
                    break
                while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'ENDWHILE':
                    self._parse_statement()
            self._expect('ENDWHILE')
        
        elif token_type == 'FOR':
            self.token_pos += 1
            var_name = self._expect('ID')[1]
            self._expect('IN')
            iterable = self._parse_expression()
            if isinstance(iterable, list):
                for item in iterable:
                    self.variables[var_name] = item
                    while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'ENDFOR':
                        self._parse_statement()
            self._expect('ENDFOR')
        
        elif token_type == 'FUNC':
            self.token_pos += 1
            func_name = self._expect('ID')[1]
            params = []
            if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == 'LPAREN':
                self.token_pos += 1
                while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'RPAREN':
                    if self.tokens[self.token_pos][0] == 'ID':
                        params.append(self.tokens[self.token_pos][1])
                        self.token_pos += 1
                    if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == 'COMMA':
                        self.token_pos += 1
                self._expect('RPAREN')
            # 解析函数体
            func_body = []
            while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'ENDFUNC':
                func_body.append(self.tokens[self.token_pos])
                self.token_pos += 1
            self.functions[func_name] = (params, func_body)
            self._expect('ENDFUNC')
        
        elif token_type == 'IMPORT':
            # 处理import语句
            self.token_pos += 1
            module_name = self._expect('ID')[1]
            # 尝试导入Python模块
            try:
                import importlib
                module = importlib.import_module(module_name)
                self.variables[module_name] = module
                print(f"✓ 成功导入Python模块: {module_name}")
                # 检查是否有分号结束
                if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == 'SEMICOLON':
                    self.token_pos += 1
            except ImportError:
                # 尝试导入自定义模块
                self._import_module(module_name)
        
        else:
            # 尝试解析表达式
            self._parse_expression()
    
    def _import_module(self, module_name):
        """导入模块"""
        import os
        # 尝试不同的文件路径
        module_paths = [
            f"mode/{module_name}.BMDe",
            f"mode/{module_name}.bmde",
            f"{module_name}.BMDe",
            f"{module_name}.bmde"
        ]
        
        for path in module_paths:
            if os.path.exists(path):
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        module_code = f.read()
                    
                    # 词法分析模块代码
                    module_lexer = Lexer(module_code)
                    module_tokens = module_lexer.tokenize()
                    
                    # 执行模块代码
                    old_pos = self.token_pos
                    old_tokens = self.tokens
                    self.tokens = module_tokens
                    self.token_pos = 0
                    
                    try:
                        while self.token_pos < len(self.tokens):
                            self._parse_statement()
                    except Exception as e:
                        # 忽略模块执行中的错误，继续执行
                        pass
                    
                    # 恢复原有的token位置和tokens
                    self.tokens = old_tokens
                    self.token_pos = old_pos
                    print(f"✓ 成功导入模块: {module_name}")
                    return
                except Exception as e:
                    print(f"Error: 导入模块 {module_name} 失败: {e}")
                    return
        
        print(f"Error: 模块 {module_name} 未找到")
    
    def _parse_expression(self):
        return self._parse_additive()
    
    def _parse_additive(self):
        left = self._parse_multiplicative()
        while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] in ['ADD', 'SUB']:
            op = self.tokens[self.token_pos][0]
            self.token_pos += 1
            right = self._parse_multiplicative()
            if op == 'ADD':
                left = left + right
            elif op == 'SUB':
                left = left - right
        return left
    
    def _parse_multiplicative(self):
        left = self._parse_unary()
        while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] in ['MUL', 'DIV', 'MOD']:
            op = self.tokens[self.token_pos][0]
            self.token_pos += 1
            right = self._parse_unary()
            if op == 'MUL':
                left = left * right
            elif op == 'DIV':
                left = left / right
            elif op == 'MOD':
                left = left % right
        return left
    
    def _parse_unary(self):
        if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == 'SUB':
            self.token_pos += 1
            return -self._parse_primary()
        return self._parse_primary()
    
    def _parse_primary(self):
        token_type, token_value = self.tokens[self.token_pos]
        
        if token_type == 'NUMBER':
            self.token_pos += 1
            return token_value
        
        elif token_type == 'STRING':
            self.token_pos += 1
            return token_value
        
        elif token_type == 'NONE':
            self.token_pos += 1
            return None
        
        elif token_type == 'TRUE':
            self.token_pos += 1
            return True
        
        elif token_type == 'FALSE':
            self.token_pos += 1
            return False
        
        elif token_type == 'ID':
            self.token_pos += 1
            if token_value in self.variables:
                return self.variables[token_value]
            elif token_value in self.functions:
                # 处理函数调用
                params = []
                if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == 'LPAREN':
                    self.token_pos += 1
                    while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'RPAREN':
                        params.append(self._parse_expression())
                        if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == 'COMMA':
                            self.token_pos += 1
                    self._expect('RPAREN')
                # 执行函数
                func_params, func_body = self.functions[token_value]
                # 保存当前变量状态
                old_vars = self.variables.copy()
                # 设置函数参数
                for i, param in enumerate(func_params):
                    if i < len(params):
                        self.variables[param] = params[i]
                # 执行函数体
                for token in func_body:
                    # 处理return语句
                    if token[0] == 'RETURN':
                        return_val = self._parse_expression()
                        # 恢复变量状态
                        self.variables = old_vars
                        return return_val
                # 恢复变量状态
                self.variables = old_vars
                return None
            else:
                print(f"Error: Variable or function {token_value} not defined")
                return None
        
        elif token_type == 'LPAREN':
            self.token_pos += 1
            expr = self._parse_expression()
            self._expect('RPAREN')
            return expr
        
        elif token_type == 'STR':
            self.token_pos += 1
            self._expect('LPAREN')
            value = self._parse_expression()
            self._expect('RPAREN')
            return str(value)
        
        elif token_type == 'INT':
            self.token_pos += 1
            self._expect('LPAREN')
            value = self._parse_expression()
            self._expect('RPAREN')
            return int(value)
        
        elif token_type == 'FLOAT':
            self.token_pos += 1
            self._expect('LPAREN')
            value = self._parse_expression()
            self._expect('RPAREN')
            return float(value)
        
        elif token_type == 'LIST':
            self.token_pos += 1
            self._expect('LPAREN')
            items = []
            while self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] != 'RPAREN':
                items.append(self._parse_expression())
                if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == 'COMMA':
                    self.token_pos += 1
            self._expect('RPAREN')
            return items
        
        elif token_type == 'LEN':
            self.token_pos += 1
            self._expect('LPAREN')
            value = self._parse_expression()
            self._expect('RPAREN')
            return len(value)
        
        elif token_type == 'MAX':
            self.token_pos += 1
            self._expect('LPAREN')
            value = self._parse_expression()
            self._expect('RPAREN')
            return max(value)
        
        elif token_type == 'MIN':
            self.token_pos += 1
            self._expect('LPAREN')
            value = self._parse_expression()
            self._expect('RPAREN')
            return min(value)
        
        elif token_type == 'SUM':
            self.token_pos += 1
            self._expect('LPAREN')
            value = self._parse_expression()
            self._expect('RPAREN')
            return sum(value)
        
        elif token_type == 'RAND':
            self.token_pos += 1
            self._expect('LPAREN')
            self._expect('RPAREN')
            return random.random()
        
        else:
            self.token_pos += 1
            return None
    
    def _expect(self, token_type):
        if self.token_pos < len(self.tokens) and self.tokens[self.token_pos][0] == token_type:
            token = self.tokens[self.token_pos]
            self.token_pos += 1
            return token
        else:
            expected = token_type
            found = self.tokens[self.token_pos][0] if self.token_pos < len(self.tokens) else 'EOF'
            print(f"Error: Expected {expected}, found {found}")
            return None

# 主函数
def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python banana_interpreter_simple.py <file.baNa>")
        return
    
    file_path = sys.argv[1]
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # 词法分析
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        # 语法分析和执行
        interpreter = Interpreter()
        interpreter.parse(tokens)
        
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
