class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, *args) -> str:
        if 1 == len(args):
            return args[0].upper()
        else:
            return ''.join(args)



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
