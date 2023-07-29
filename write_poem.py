def write_poem(sentence1: list)-> str:
    poem = '\n'.join(sentence1)
    return poem

if __name__ == '__main__':
    sentence1 =\
        [
            '11111', 
            '22222',
            'xxxxx',
            'yyyii',
            'zzzmm'
        ]
    print(write_poem(sentence1))