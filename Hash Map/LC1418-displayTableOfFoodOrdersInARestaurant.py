class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = defaultdict(lambda: defaultdict(int))
        foods_set = set()
        for name, table, food in orders:
            d[table][food] += 1
            foods_set.add(food)
        
        foods_list = sorted(foods_set)
        result = [['Table'] + [food for food in foods_list]]
        for table in sorted(d, key=int):
            result.append([table] + [str(d[table][food]) for food in foods_list])
        return result