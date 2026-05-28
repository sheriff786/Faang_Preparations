"""
=============================================================
PYTHON LOOPS - COMPLETE TUTORIAL (Hindi + English Explanation)
=============================================================
Java se aaye ho? Tension mat lo! 
Python loops bahut simple hain, bas syntax thoda different hai.

JAVA vs PYTHON - Quick Comparison:
    Java:  for(int i=0; i<5; i++) { ... }
    Python: for i in range(5):  ...

    Java:  while(condition) { ... }
    Python: while condition: ...

Key Difference: Python mein curly braces {} nahi hote,
                INDENTATION (spaces) se block define hota hai!
=============================================================
"""

# ============================================================
# 1. FOR LOOP - Basics
# ============================================================
# Java mein: for(int i=0; i<5; i++) { System.out.println(i); }
# Python mein: range() use karte hain

print("=" * 50)
print("1. BASIC FOR LOOP (range)")
print("=" * 50)

# range(5) matlab -> 0, 1, 2, 3, 4  (5 tak nahi, 5 SE PEHLE tak)
# Java jaisa: for(int i=0; i<5; i++)
for i in range(5):
    print(i, end=" ")
print()  # new line

# Yaad rakho: range(5) = [0, 1, 2, 3, 4]  -> 0 se start, 5 EXCLUDED

print("\n--- range(start, stop) ---")
# range(2, 7) matlab -> 2, 3, 4, 5, 6  (7 excluded hai!)
# Java jaisa: for(int i=2; i<7; i++)
for i in range(2, 7):
    print(i, end=" ")
print()

print("\n--- range(start, stop, step) ---")
# range(0, 10, 2) matlab -> 0, 2, 4, 6, 8  (step 2 se badhega)
# Java jaisa: for(int i=0; i<10; i+=2)
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# REVERSE loop - Ulta chalna hai!
# range(5, 0, -1) matlab -> 5, 4, 3, 2, 1
# Java jaisa: for(int i=5; i>0; i--)
print("\n--- Reverse loop ---")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

"""
RANGE() FORMULA - Yaad rakh lo:
    range(stop)             -> 0 se stop-1 tak
    range(start, stop)      -> start se stop-1 tak
    range(start, stop, step)-> start se stop-1 tak, step gap mein
    
    STOP hamesha EXCLUDED hota hai! (Java mein < condition jaisa)
"""


# ============================================================
# 2. FOR LOOP - Iterating over Collections (PYTHON KI TAAKAT!)
# ============================================================
print("\n" + "=" * 50)
print("2. FOR LOOP ON COLLECTIONS (Lists, Strings, etc.)")
print("=" * 50)

# Java mein: for(String fruit : fruits) { ... }  (enhanced for loop)
# Python mein: EXACTLY same concept, but simpler syntax

fruits = ["apple", "banana", "mango", "grapes"]

# Direct iteration - Sabse common & Pythonic way
print("\n--- Direct iteration (sabse simple!) ---")
for fruit in fruits:
    print(fruit)

# Agar INDEX bhi chahiye saath mein -> enumerate() use karo
# Java mein: for(int i=0; i<fruits.length; i++) { fruits[i] }
print("\n--- enumerate() - index + value dono milega ---")
for index, fruit in enumerate(fruits):
    print(f"  index {index} -> {fruit}")

# String pe loop - Har character pe jaayega
print("\n--- String pe loop ---")
name = "Python"
for char in name:
    print(char, end=" ")
print()

# Dictionary pe loop
print("\n--- Dictionary pe loop ---")
student = {"name": "Rahul", "age": 25, "city": "Delhi"}

# Sirf keys
print("Keys:")
for key in student:
    print(f"  {key}")

# Keys + Values dono
print("Keys + Values:")
for key, value in student.items():
    print(f"  {key} = {value}")


# ============================================================
# 3. WHILE LOOP
# ============================================================
print("\n" + "=" * 50)
print("3. WHILE LOOP")
print("=" * 50)

# Java:  int i=0; while(i<5) { print(i); i++; }
# Python: Same concept, bas syntax different

print("\n--- Basic while loop ---")
i = 0
while i < 5:
    print(i, end=" ")
    i += 1  # Python mein i++ NAHI hota! i += 1 likhna padta hai
print()

# IMPORTANT: Python mein i++, i--, ++i, --i KUCH BHI NAHI HOTA!
# Hamesha i += 1 ya i -= 1 likhna hai

print("\n--- While with condition ---")
num = 100
while num > 1:
    print(num, end=" ")
    num //= 2  # integer division (Java mein num = num / 2 jaisa)
print()


# ============================================================
# 4. BREAK, CONTINUE, PASS
# ============================================================
print("\n" + "=" * 50)
print("4. BREAK, CONTINUE, PASS")
print("=" * 50)

# BREAK - Loop se bahar nikal jao (Java jaisa hi hai)
print("\n--- break: loop tod do ---")
for i in range(10):
    if i == 5:
        break  # 5 aate hi loop khatam
    print(i, end=" ")
print("  <- loop stopped at 5")

# CONTINUE - Is iteration ko skip karo, agle pe jao (Java jaisa)
print("\n--- continue: skip karo ---")
for i in range(10):
    if i % 2 == 0:
        continue  # even numbers skip
    print(i, end=" ")  # sirf odd print honge
print("  <- only odd numbers")

# PASS - Kuch mat karo (placeholder, Java mein koi equivalent nahi)
print("\n--- pass: kuch mat karo (placeholder) ---")
for i in range(5):
    if i == 3:
        pass  # abhi kuch nahi karna, baad mein code add karenge
    print(i, end=" ")
print("  <- pass does nothing, loop continues")


# ============================================================
# 5. NESTED LOOPS (Loop ke andar Loop)
# ============================================================
print("\n" + "=" * 50)
print("5. NESTED LOOPS")
print("=" * 50)

# Java: for(int i=0;i<3;i++) { for(int j=0;j<3;j++) {...} }
# Pattern printing - Interview mein bahut aata hai!

print("\n--- Star Pattern (Right Triangle) ---")
for i in range(1, 6):       # i = 1,2,3,4,5 (rows)
    for j in range(i):      # j = 0 to i-1 (columns in each row)
        print("*", end=" ")
    print()  # new line after each row

print("\n--- Multiplication Table (2 to 4) ---")
for i in range(2, 5):       # tables of 2, 3, 4
    for j in range(1, 6):   # multiply by 1 to 5
        print(f"{i}x{j}={i*j}", end="\t")
    print()


# ============================================================
# 6. LIST COMPREHENSION (Python ki Special Trick!)
# ============================================================
print("\n" + "=" * 50)
print("6. LIST COMPREHENSION (Short loop in one line!)")
print("=" * 50)

# Java mein:
#   List<Integer> squares = new ArrayList<>();
#   for(int i=0; i<5; i++) { squares.add(i*i); }
#
# Python mein EK LINE mein ho jaata hai! 

# Normal way:
squares_normal = []
for i in range(5):
    squares_normal.append(i * i)

# List Comprehension way (SAME result, ek line!):
squares_lc = [i * i for i in range(5)]

print(f"  Normal loop:        {squares_normal}")
print(f"  List comprehension: {squares_lc}")

# With condition - Sirf even numbers ke squares
even_squares = [i * i for i in range(10) if i % 2 == 0]
print(f"  Even squares: {even_squares}")

"""
LIST COMPREHENSION FORMULA:
    [expression FOR variable IN iterable IF condition]
    
    Padho aise: "har variable ke liye jo iterable mein hai,
                 agar condition true hai, to expression do"
    
    Example: [i*i for i in range(10) if i%2==0]
    Matlab:  "har i ke liye 0 se 9 tak, agar i even hai, to i*i do"
"""


# ============================================================
# 7. COMMON PATTERNS (Interview mein aate hain!)
# ============================================================
print("\n" + "=" * 50)
print("7. COMMON LOOP PATTERNS")
print("=" * 50)

# Pattern 1: Array traverse with index
print("\n--- Array traverse (with index) ---")
arr = [10, 20, 30, 40, 50]
# Java style (works but NOT Pythonic):
for i in range(len(arr)):
    print(f"  arr[{i}] = {arr[i]}")

# Pattern 2: Two pointer (interview favourite!)
print("\n--- Two Pointer Pattern ---")
arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1
while left < right:
    print(f"  left={arr[left]}, right={arr[right]}")
    left += 1
    right -= 1

# Pattern 3: Loop with else (Python SPECIAL - Java mein nahi hai!)
print("\n--- for...else (Python special!) ---")
# else block tab chalega jab loop NORMALLY khatam ho (break nahi hua)
for i in range(5):
    if i == 10:  # ye condition kabhi true nahi hogi
        break
else:
    print("  Loop completed without break! (else executed)")

# Agar break hota:
for i in range(5):
    if i == 3:
        break
else:
    print("  This won't print because break happened")
print("  Break hua at i=3, so else did NOT execute")

# Pattern 4: zip() - Do lists ko saath mein traverse karo
print("\n--- zip() - parallel iteration ---")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
# Java mein do arrays ko saath traverse karna mushkil hai
# Python mein zip() se ek line!
for name, score in zip(names, scores):
    print(f"  {name}: {score}")


# ============================================================
# 8. INFINITE LOOP & COMMON MISTAKES
# ============================================================
print("\n" + "=" * 50)
print("8. COMMON MISTAKES (Dhyan rakho!)")
print("=" * 50)

print("""
MISTAKE 1: i++ likhna (Python mein NAHI hota!)
    WRONG:  i++
    RIGHT:  i += 1

MISTAKE 2: range mein stop INCLUDED samajhna
    range(5) = [0,1,2,3,4]  -> 5 INCLUDED NAHI HAI!
    Agar 1 se 5 tak chahiye: range(1, 6)  -> 6 excluded, 5 included

MISTAKE 3: Indentation galat karna
    WRONG:                      RIGHT:
    for i in range(5):          for i in range(5):
    print(i)  # ERROR!              print(i)  # 4 spaces indent

MISTAKE 4: List modify karte waqt iterate karna
    WRONG:
    for item in my_list:
        my_list.remove(item)  # DANGEROUS! Unexpected behavior
    
    RIGHT:
    for item in my_list[:]:   # copy pe iterate karo
        my_list.remove(item)

MISTAKE 5: while loop mein counter update bhoolna
    WRONG:                      RIGHT:
    i = 0                       i = 0
    while i < 5:                while i < 5:
        print(i)                    print(i)
        # i update bhool gaye!     i += 1  # ZARURI HAI!
        # INFINITE LOOP!
""")


# ============================================================
# 9. JAVA vs PYTHON - Quick Reference Card
# ============================================================
print("=" * 50)
print("9. JAVA vs PYTHON - LOOP CHEAT SHEET")
print("=" * 50)
print("""
╔══════════════════════════════════════════════════════════════╗
║  JAVA                          PYTHON                       ║
╠══════════════════════════════════════════════════════════════╣
║  for(int i=0;i<n;i++)          for i in range(n):           ║
║  for(int i=a;i<b;i++)          for i in range(a, b):        ║
║  for(int i=0;i<n;i+=2)         for i in range(0, n, 2):     ║
║  for(int i=n;i>0;i--)          for i in range(n, 0, -1):    ║
║  for(String s : list)          for s in list:               ║
║  while(cond) { i++; }          while cond: i += 1           ║
║  do { } while(cond);           (Python mein nahi hai!)      ║
║  i++  /  i--                   i += 1  /  i -= 1            ║
║  break;                        break                        ║
║  continue;                     continue                     ║
║  { } curly braces              : colon + indentation        ║
╚══════════════════════════════════════════════════════════════╝

REMEMBER:
  - Python mein semicolons ; optional hain (mat lagao)
  - Python mein parentheses () optional hain conditions mein
      Java:   while(i < 5)
      Python: while i < 5:    (no parentheses needed!)
  - Colon : ZARURI hai for/while/if ke baad
  - 4 spaces indentation = Java ka { } block
""")

print("\n✅ File complete! Jab bhi loops confuse kare, ye file kholo!")
print("   Run karo: python python_loops_tutorial.py")
