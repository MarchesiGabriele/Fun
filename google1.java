package google;

import java.util.HashMap;
import java.util.Map;


// Count minimum amount of inserts to make input string follow the pattern abcabcabc...

public class google1 {
	static int sol(String a) {
		  int count = 0;
		  int shouldbe = 0;
		  Map<Integer, Character> k = new HashMap<>();
		  k.put(0, 'a');
		  k.put(1, 'b');
		  k.put(2, 'c');
		  
		  int i = 0;
		  while(i < a.length()) {
		   if(k.get(shouldbe%3) != a.charAt(i)) {
		    count++;
		    shouldbe++;
		   }
		   else {
		    shouldbe++;
		    i++;
		   }
		  };
		  return count;
	}
}
