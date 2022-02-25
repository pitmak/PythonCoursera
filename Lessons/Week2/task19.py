s1, s2, s3 = int(input()), int(input()), int(input())
n1, n2, n3 = int(input()), int(input()), int(input())
print(max(
    (s1 // n1) * (s2 // n2) * (s3 // n3),
    (s1 // n1) * (s2 // n3) * (s3 // n2),
    (s1 // n2) * (s2 // n1) * (s3 // n3),
    (s1 // n2) * (s2 // n3) * (s3 // n1),
    (s1 // n3) * (s2 // n1) * (s3 // n2),
    (s1 // n3) * (s2 // n2) * (s3 // n1)
))
