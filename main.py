import trees

def main():
    list_node = [30, 60, 40, 50, 23, 45, 61]
    #заполнение дерева
    node = trees.Node(47)
    for i in list_node:
        node.insert(i)
    #вывод дерева в порядке возрастания
    node.print_wood()
    #поиск значения в дереве
    print(node.search_el(50))
    print(node.search_el(72))

if __name__ == "__main__":
    main()