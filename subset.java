package subset;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SubsetTest {
	static int N;
	
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("./input2.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(in.readLine());
		
		int[] arr = new int[N];
		boolean[] visited = new boolean[N];
		
		StringTokenizer st = new StringTokenizer(in.readLine());
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		subset(arr, visited, 0);
	}
	
	static void subset(int[] arr, boolean[] visited, int cnt) {
		if(cnt == N) {
			for(int i = 0; i < N; i++) {
				if(visited[i]) System.out.print(arr[i]+" ");
			}
			System.out.println();
			return;
		}
		
		// 원소 선택
		visited[cnt] = true;
		subset(arr, visited, cnt+1);
					
		// 원소 미선택
		visited[cnt] = false;
		subset(arr, visited, cnt+1);
	}
}
