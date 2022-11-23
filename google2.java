package google;

import java.util.Set;
import java.util.TreeMap;

// Given list of side lengths create rectangles and get minimum absolute value of the difference between 2 length of rectangle sides. 

public class google2 {
	static int sol(int[] list) {
		TreeMap<Integer, Integer> k = new TreeMap<>();
		
		for(int i = 0; i<list.length; i++){
			if(k.containsKey(list[i])) {
				int prev = k.get(list[i]) +1;
				if(prev == 4) 
					return 0;
				k.replace(list[i], prev);
			}else {
				k.put(list[i], 1);
			}
		}
		
		
		int key1 = -1;
		int key2 = -1;
		int min = Integer.MAX_VALUE; 
		Set<Integer> m = k.keySet();
	
		for(Integer o : m) {
			if(k.get(o)>=2) {
				key2 = key1;
				key1 = o;
			}
			
			int aa; 
			if(key1 != -1 && key2 != -1) {
				aa =  Math.abs(key2-key1);
			
				if(aa<min) {
					min = aa;
				}
			}
	}
		
		return min == Integer.MAX_VALUE ? -1 : min;
	}
}
