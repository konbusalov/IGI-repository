from services.matrix_analyzer import MatrixAnalyzer

def task5():
    analyzer = MatrixAnalyzer(5, 5)
    
    results = analyzer.analyze()
    
    print("-"*148)
    print("Исходная матрица:")
    print(results['matrix'])
    print("\nПобочная диагональ:", results['secondary_diagonal'])
    print("Минимальный элемент на побочной диагонали:", results['min_secondary'])
    print("Дисперсия побочной диагонали (numpy/формула):", results['variance'])
    print("\nСреднее значение элементов матрицы:", results['mean'])
    print("Медиана элементов матрицы:", results['median'])
    print("Стандартное отклонение элементов матрицы:", results['std'])
    print("\nМатрица корреляции:")
    print(results['correlation'])
    print("-"*148)
