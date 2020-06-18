# Author:HeartMaster
# 创建字典方法1
Trie = {"a": "$",
        "b": {
            "c":
                {"g": "$", "h": "$"},
            "e":
                {"i": "$", "j": "$"},
            "f":
                {"k": "$", "l": "$"},
        }}

# 创建字典方法2
lst = ['a', 'bcg', 'bch', 'bei', 'bej', 'bfk', 'bfl']
Trie = {}

for i in lst:
    cur_node = Trie
    for x in i[:-1]:
        if x not in cur_node:
            cur_node[x] = {}
        cur_node = cur_node[x]
    cur_node[i[-1]] = '$'

print(Trie)

# 在字典树中搜索单词是否存在
def search(word):
    cur_node = Trie
    for i in word:
        try:
            cur_node = cur_node[i]
        except:
            return False
    return True if cur_node == '$' else False

# 路径不存在于字典的情况
print(search('bce'))
# 路径不是完整的单词的情况
print(search('b'))
# 路径是合理的单词的情况
print(search('a'))
print(search('bgj'))



# 寻找以broken_word为开头，一直到叶节点的每个路径
def get_start_with(broken_word):
    # 以字符串为路径找到最后一个字符在字典中的节点
    cur_node = Trie
    for i in broken_word:
        try:
            cur_node = cur_node[i]
        # 路径不存在字典中，则直接返回原词
        except:
            return [broken_word]

    # 递归遍历字典树，pre_string传入'',cur_node传入root，这个方法将打印整个字典
    def get_completion_words(pre_string, cur_node):
        word_list = []
        # 叶节点退出递归，返回完整字符串
        if cur_node == '$':
            word_list.append(pre_string)
            return word_list
        # 通过字典树的每个分支对之前的字符串进行补充
        for key in list(cur_node):
            word_list.extend(get_completion_words(pre_string + str(key), cur_node[key]))
        # 返回最终结果
        return word_list

    return get_completion_words(broken_word, cur_node)


# 不存在的情况
print(get_start_with('ag'))
# 可以拓展的情况
print(get_start_with('bg'))
print(get_start_with('b'))
print(get_start_with('bfa'))

# 利用递归遍历了整个字典树
print(get_start_with(''))
