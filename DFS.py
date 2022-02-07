class Dfs:
    def __init__(self):
        self.res_list = []

    def sample(self, root):
        self.res_list.append(root)
        root_child = int(input(f"Enter the number of child nodes for {root}: "))
        self.dfs(root_child)
        return " ".join(self.res_list)

    def dfs(self, root_child):
        list_of = list(map(str, input("Enter the children: ").split()))
        for i in range(root_child):
            value = int(input(f"Enter the number of children for {list_of[i]}: "))
            if value == 0:
                self.res_list.append(list_of[i])
                i += 1
            else:
                self.res_list.append(list_of[i])
                self.dfs(value)


dfs = Dfs()
print(dfs.sample(input("Enter the root node: ")))
