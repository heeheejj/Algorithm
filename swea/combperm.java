package permutation_combination;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class PermutationCombinationTest {
	static int N, R;
	public static void main(String[] args) throws IOException {
		// 입출력 연습~!
		System.setIn(new FileInputStream("./input.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		N = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[N];
		int[] out = new int[R];
		boolean[] visited = new boolean[N];
		
		st = new StringTokenizer(in.readLine());
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		System.out.println("============순열============");
		init(out, visited);
		perm(arr, out, visited, 0);
		System.out.println("============중복순열============");
		init(out, visited);
		permWithRepetition(arr, out, 0);
		System.out.println("============조합============");
		init(out, visited);
		comb(arr, visited, 0, 0);
		System.out.println("============중복조합============");
		init(out, visited);
		combWithRepetition(arr, out, 0, 0);
		
	}
	
	static void init(int[] out, boolean[] visited) {
		Arrays.fill(out, 0);
		Arrays.fill(visited, false);
	}
	
	static void perm(int[] arr, int[] out, boolean[] visited, int cnt) {
		if(cnt == R) {
			System.out.println(Arrays.toString(out));
			return;
		}
		
		for(int i = 0; i < N; i++) {
			if(!visited[i]) {
				visited[i] = true;
				out[cnt] = arr[i];
				perm(arr, out, visited, cnt+1);
				visited[i] = false;
			}
		}
	}
	
	static void permWithRepetition(int[] arr, int[] out, int cnt) {
		if(cnt == R) {
			System.out.println(Arrays.toString(out));
			return;
		}
		
		for(int i = 0; i < N; i++) {
			out[cnt] = arr[i];
			permWithRepetition(arr, out, cnt+1);
		}
	}
	
	static void comb(int[] arr, boolean[] visited, int start, int cnt) {
		if(cnt == R) {
			for(int i = 0; i < N; i++) {
				if(visited[i]) System.out.print(arr[i]+" ");
			}
			System.out.println();
			return;
		}
		
		for(int i = start; i < N; i++) {
			if(!visited[i]) {
				visited[i] = true;
				comb(arr, visited, i+1, cnt+1);
				visited[i] = false;
			}
		}
	}
	
	static void combWithRepetition(int[] arr, int[] out, int start, int cnt) {
		if(cnt == R) {
			System.out.println(Arrays.toString(out));
			return;
		}
		
		for(int i = start; i < N; i++) {
			out[cnt] = arr[i];
			combWithRepetition(arr, out, i, cnt+1);
		}
	}
}
