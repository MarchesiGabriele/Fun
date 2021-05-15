main() {
  List<int> c = [1, 2, 3, 4];
  f(c);
}

List<int> result = [];
List<int> newList = [];
void f(List<int> lista) {
  int index = 0;
  while (index < lista.length) {
    newList = new List<int>.from(lista);
    result.add(lista[index]);
    if (lista.length == 1) {
      print(result);
      result.removeAt(result.length - 1);
      result.removeAt(result.length - 1);
      return;
    }
    newList.removeAt(index);
    f(newList);
    index++;
  }
  if (result.length != 0) {
    result.removeAt(result.length - 1);
  }
  return;
}
