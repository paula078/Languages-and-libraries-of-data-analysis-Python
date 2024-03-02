  # 📊 Languages and Libraries of Data Analysis 📈

This repository contains materials related to the course "Languages and Libraries of Data Analysis" at AGH University of Science and Technology for the academic year 2023/24. The course aims to familiarize students with programming in Python, with a particular emphasis on its application in data analysis.

## 📝 Tasks
- **Task 1**:
  
  The goal of this task was to implement a Binary Search Tree (BST) capable of handling the following operations:
  - Adding nodes to the tree
  - Checking whether a node exists in the tree
  - Printing the nodes in ascending order using in-order traversal.
  
- **Task 2**:
  - I. Write a class 'Graph' where vertices can be immutable objects. The class should allow the following operations:
      - Adding a vertex
      - Removing a vertex (along with all adjacent edges)
      - Adding an edge
      - Removing an edge
      - Getting all neighbors of a specified vertex.

  - II. Write methods "bfs" and "dfs" which accept a vertex from which we want to start traversing the graph and allow iteration over the graph in breadth-first and depth-first order, respectively.

  
- **Task 3**:
  - I. Write a function that counts the occurrences of all words in a text file. Make it possible to display the n most frequently occurring words _with ties_.

  - II. Write functions that count the occurrences of all word n-grams in a text file. Also, allow display of top ties with ties.
    An n-gram is ANY n consecutive words (or other units, depending on the context). For example, the sentence "Ala has a cat" has two digrams: "Ala has" and "she has a cat".

  - III. Write a context manager to handle the .conll file. Iterating through the file should return subsequent lines in the form of a tuple or list.
  
- **Task 4**:
  
  The objective of this task was to design and implement a library management system. The system should be operated through the console, utilizing menus wherever possible.

  The system should allow users to log in as either a reader or a librarian.
  
  Readers should be able to:
  - Borrow a book
  - Reserve a book that is currently borrowed
  - Extend the borrowing period
  - Browse the catalog (search by title, author, or keywords)
  
  Librarians should be able to:
  - Accept book returns
  - Add a new book
  - Remove a book from the system
  - Add a new reader
  - Browse the catalog
    
  The system should store its data on disk, and changes made during one program session should be visible in the next session. 
  
- **Task 5**:
 
  The objective of this task was to implement the k-nearest neighbors (kNN) binary classification algorithm.

  The implemented class should provide methods train and predict.
  
  The train method builds the training set (accepting at least vectors and correct labels). Multiple calls to the train method should extend the training set.
  The predict method accepts a vector (optionally: multiple vectors at once) and returns the classifier's response.
  It should be possible to choose one of four distance functions: Euclidean, Manhattan, Chebyshev, and Cosine.

- **Task 6**:
  
  Using the pandas library:
  - Load the file EURUSD30.csv (source: Kaggle). The successive columns are: DateTime, Open, High, Low, Close, Volume.
  - Filter out rows with missing data.
  - Create a DataFrame containing the same data, but on a daily basis.
  - Create a data series containing the percentage increase (or decrease) in the exchange rate on a given day (as the difference between Open and Close).
  - Calculate the mean and standard deviation of this column and plot a histogram.
  - Repeat steps 4 and 5 for increases over three days. Note: If one reading contains the difference between the opening on Monday and the closing on Wednesday, then the next    reading should be the difference between the opening on Tuesday and the closing on Thursday.
