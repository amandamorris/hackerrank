def array_left_rotation(a, n, k):
    """for each index, new index is ((index + k) mod a) """
    a = [a[(i + k) % n] for i in range(n)]
    print a

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))