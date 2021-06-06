/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/

import 'dart:collection';

main(List<String> args) {
  int target = 6;
  List<int> l = [2, 5, 7, 1, 8];
  print(f(l, target));
  print(f2(l, target));
}

//Easy Way
List<int> f(List<int> list, int tg) {
  List<int> newList = List.from(list);
  for (;;) {
    if (newList.contains(tg - newList[0])) {
      return [list.indexOf(newList[0]), list.indexOf(tg - newList[0])];
    } else {
      newList.removeAt(0);
    }
  }
}

//The key is the missing value, if I find one this is the couple i was looking for
List<int?>? f2(List<int> list, int tg) {
  HashMap<int, int> map = new HashMap();
  for (int i = 0; i < list.length; i++) {
    map[tg - list[i]] = i;
    if (map.containsKey(list[i])) {
      return [map[list[i]], i];
    }
  }
}
