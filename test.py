import unittest
import bfs


class TestBFSTree(unittest.TestCase):
    
    def test1(self):
        """Одна вершина"""
        n = 1
        adjacency_matrix = [[0]]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(T, set())
        self.assertEqual(B, set())
        self.assertEqual(Dnum, {0: 1})
    
    def test2(self):
        """Две вершины, соединенные ребром"""
        n = 2
        adjacency_matrix = [
            [0, 1],
            [1, 0]
        ]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(T, {(0, 1)})
        self.assertEqual(B, set())
        self.assertEqual(Dnum, {0: 1, 1: 2})
    
    def test3(self):
        """Цепочка из 3 вершин: 0-1-2"""
        n = 3
        adjacency_matrix = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(T, {(0, 1), (1, 2)})
        self.assertEqual(B, set())
        self.assertEqual(Dnum, {0: 1, 1: 2, 2: 3})
    
    def test4(self):
        """Треугольник (цикл из 3 вершин)"""
        n = 3
        adjacency_matrix = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(T, {(0, 1), (0, 2)})
        self.assertEqual(B, {(1, 2)})
        self.assertEqual(Dnum, {0: 1, 1: 2, 2: 3})
    
    def test5(self):
        """Цикл из 4 вершин: 0-1-2-3-0"""
        n = 4
        adjacency_matrix = [
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
        ]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(T, {(0, 1), (0, 3), (1, 2)})
        self.assertEqual(B, {(2, 3)})
        self.assertEqual(Dnum, {0: 1, 1: 2, 3: 3, 2: 4})
    
    def test6(self):
        """Звезда с центром в вершине 0"""
        n = 4
        adjacency_matrix = [
            [0, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0]
        ]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(T, {(0, 1), (0, 2), (0, 3)})
        self.assertEqual(B, set())
        self.assertEqual(Dnum, {0: 1, 1: 2, 2: 3, 3: 4})

    def test7(self):
        """Бант"""
        n = 5
        adjacency_matrix = [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0]
        ]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(T, {(0, 1), (0, 2), (2, 3), (2, 4)})
        self.assertEqual(B, {(1, 2), (3, 4)})
        self.assertEqual(Dnum, {0: 1, 1: 2, 2: 3, 3: 4, 4: 5})


    def test8(self):
        """Полный граф K4 (4 вершины)"""
        n = 4
        adjacency_matrix = [
            [0, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 0]
        ]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(T, {(0, 1), (0, 2), (0, 3)})
        self.assertEqual(B, {(1, 2), (1, 3), (2, 3)})
        self.assertEqual(Dnum, {0: 1, 1: 2, 2: 3, 3: 4})

    def test9(self):
        """Два треугольника, соединенных мостом (6 вершин)"""
        n = 6
        adjacency_matrix = [
            [0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 1, 1],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 0]
        ]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(T, {(0, 1), (0, 2), (2, 3), (3, 4), (3, 5)})
        self.assertEqual(B, {(1, 2), (4, 5)})
        self.assertEqual(Dnum, {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6})

    def test10(self):
        """Сетка 3x3 (9 вершин), старт из центра"""
        n = 9
        # Формируем матрицу смежности для сетки 3x3
        grid = [[0]*9 for _ in range(9)]
        edges = [
            # Горизонтальные ребра
            (0,1), (1,2), (3,4), (4,5), (6,7), (7,8),
            # Вертикальные ребра
            (0,3), (3,6), (1,4), (4,7), (2,5), (5,8)
        ]
        for u, v in edges:
            grid[u][v] = 1
            grid[v][u] = 1
        
        a = 4
        
        T, B, Dnum = bfs.bfs_tree(n, grid, a)
        
        expected_T = {(1,4), (3,4), (4,5), (4,7), (0,1), (1,2), (3,6), (5,8)}
        expected_B = {(0,3), (2,5), (6,7), (7,8)}
        expected_Dnum = {4:1, 1:2, 3:3, 5:4, 7:5, 0:6, 2:7, 6:8, 8:9}
        
        self.assertEqual(T, expected_T)
        self.assertEqual(B, expected_B)
        self.assertEqual(Dnum, expected_Dnum)

    def test11(self):
        """Звезда с дополнительными ребрами (7 вершин)"""
        n = 7
        adjacency_matrix = [
            [0, 1, 1, 1, 1, 1, 1],  # Центр 0 соединен со всеми
            [1, 0, 1, 0, 0, 0, 0],  # Доп. ребро между 1-2
            [1, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0],  # Доп. ребро между 3-4
            [1, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1],  # Доп. ребро между 5-6
            [1, 0, 0, 0, 0, 1, 0]
        ]
        a = 0
        
        T, B, Dnum = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(len(T), 6)
        self.assertTrue(all((0, i) in T for i in range(1, 7)))
        self.assertEqual(B, {(1,2), (3,4), (5,6)})
        self.assertEqual(Dnum[0], 1)
        self.assertEqual(set(Dnum.values()), set(range(1, 8)))

    def test12(self):
        """Цикл с хордами (8 вершин)"""
        n = 8
        adjacency_matrix = [[0]*8 for _ in range(8)]
        # Основной цикл 0-1-2-3-4-5-6-7-0
        cycle_edges = [(i, (i+1)%8) for i in range(8)]
        # Хорды: 0-4, 1-5, 2-6, 3-7
        chord_edges = [(0,4), (1,5), (2,6), (3,7)]
        
        for u, v in cycle_edges + chord_edges:
            adjacency_matrix[u][v] = 1
            adjacency_matrix[v][u] = 1
        
        a = 0
        
        T, B, _ = bfs.bfs_tree(n, adjacency_matrix, a)
        
        self.assertEqual(len(T), 7)
        self.assertTrue((0,1) in T or (0,7) in T)
        self.assertTrue((0,4) in T)
        chord_set = {(min(u,v), max(u,v)) for u,v in chord_edges}
        self.assertTrue(len(B.intersection(chord_set)) >= 2)

if __name__ == "__main__":
    unittest.main()