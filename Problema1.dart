/*Design an algorithm which takes a positive integer representing a length of rope. This rope can be divided into any number of smaller 
integer lengths. Return the maximum product you can get from multiplying the smaller lengths*/

main() {
  int n = 15;
  print("lunghezza corda iniziale: $n");
  print("Prodotto massimo: ${f(n)}");
}

int max = 0;

int f(int i) {
  List<int> c1 = List.filled(i, 1);
  m(c1, 1);
  return max;
}

void m(List<int> c1, int multAtt) {
  List<int> k1 = new List<int>.from(c1);
  List<int> k2 = [];

  while (k1.length >= c1.length ~/ 2) {
    k1.removeLast();
    k2.add(1);
    int multAtto = k2.length * multAtt;

    if (multAtto * k1.length > max) {
      max = multAtto * k1.length;
    }

    if (k1.length == 2) {
      return;
    }

    m(k1, multAtto);
  }
  return;
}
