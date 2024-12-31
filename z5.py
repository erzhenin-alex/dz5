#Ерженин Александр ДПИ23-1с

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class MyBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Добавляем новое значение в дерево."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_helper(self.root, value)

    def _insert_helper(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_helper(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_helper(node.right, value)

    def get_average(self):
        """Вычисляет среднее арифметическое всех вершин."""
        total, count = self._sum_and_count(self.root)
        return total / count if count > 0 else 0

    def _sum_and_count(self, node):
        if node is None:
            return 0, 0
        left_sum, left_count = self._sum_and_count(node.left)
        right_sum, right_count = self._sum_and_count(node.right)
        return node.value + left_sum + right_sum, 1 + left_count + right_count

    def add_average(self):
        """Добавляет в дерево вершину со значением среднего арифметического."""
        avg = self.get_average()
        print(f"Добавляю среднее значение: {avg}")
        self.insert(avg)

    def print_tree_with_types(self):
        """Выводит дерево с классификацией узлов."""
        if self.root is None:
            print("Дерево пустое")
            return

        def classify(node):
            if node == self.root:
                return 'Корень'
            elif node.left is None and node.right is None:
                return 'Лист'
            else:
                return 'Промежуточный'

        def traverse_and_print(node):
            if node:
                node_type = classify(node)
                print(f'Значение: {node.value}, Тип: {node_type}')
                traverse_and_print(node.left)
                traverse_and_print(node.right)

        traverse_and_print(self.root)

    def find_extreme(self, find_max=True):
        """Находит максимум или минимум в дереве."""
        if self.root is None:
            return None
        current = self.root
        while (current.left if not find_max else current.right) is not None:
            current = current.left if not find_max else current.right
        return current.value

    def print_leaf_values(self):
        """Выводит значения всех листьев дерева."""
        print("Листья дерева:")
        self._print_leaves(self.root)

    def _print_leaves(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.value)
            self._print_leaves(node.left)
            self._print_leaves(node.right)


# Пример использования
my_tree = MyBinaryTree()
for num in [10, 5, 15, 3, 7, 20]:
    my_tree.insert(num)

# Среднее арифметическое
average = my_tree.get_average()
print("Среднее арифметическое дерева:", average)

# Добавляем среднее значение
my_tree.add_average()

# Печатаем дерево с типами узлов
print("Дерево после добавления среднего значения:")
my_tree.print_tree_with_types()

# Максимум и минимум
print("Максимальное значение:", my_tree.find_extreme(find_max=True))
print("Минимальное значение:", my_tree.find_extreme(find_max=False))

# Листья
my_tree.print_leaf_values()
