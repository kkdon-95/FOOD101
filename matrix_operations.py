import numpy as np

def matrix_operation():
    print("Enter data for array1")
    rows1=int(input("Enter number of rows:"))
    columns1=int(input("Enter number of columns:"))
    elements1=list(map(int,input("Enter the required no of elements with a comma: ").split(",")))
    array1=np.array(elements1).reshape(rows1,columns1)

    print("Enter data for array2")
    rows2=int(input("Enter number of rows:"))
    columns2=int(input("Enter number of columns:"))
    elements2=list(map(int,input("Enter the required no of elements with a comma: ").split(",")))
    array2=np.array(elements2).reshape(rows2,columns2)

    print("array1:",array1)
    print("array2:",array2)
    
    operations=('dot','matrix','determinant')
    print(f"Choose an operation:{operations}")
    operation=input("Enter the operation:")
    if operation not in operations:
        print("Kindly chose a valid option")
        matrix_operation()

    else:
        if operation=="dot":
            if np.shape(array1) != np.shape(array2):
                print("Kindly give equal shaped array.\nTry Again")
                matrix_operation()
            if np.shape(array1)==np.shape(array2):
                print("Dot Product:",array1*array2)



        elif operation=="matrix":
            if columns1==rows2:
                resultant=np.zeros((rows1,columns2))
                for i in range(rows1):
                    for j in range(columns2):
                        for k in range(columns1):
                            resultant[i][j]=resultant[i][j]+array1[i][k]*array2[k][j]
                print("The final result is:",resultant)                       
            if columns1!=rows2: 
                print("Cannot be matrix multiplied.Try Again")  
                matrix_operation() 



        elif operation=="determinant":
            if rows1==columns1 and rows2==columns2:
                 print(int(np.linalg.det(array1)))
                 print(int(np.linalg.det(array2)))
            else:
                print("ERROR404 n0t A sQaUre maTrix")


        
matrix_operation()                       