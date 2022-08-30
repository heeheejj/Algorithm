package bfs_dfs;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class BfsTest {
// 정점개수 N과 간선개수 E를 각각 한줄로 입력받는다.
	// 다음 줄 부터(세번쨰 줄 부터) E개의 줄에 인접한 정점 두 개씩 한줄로 입력받는다. (무방향)
	// 방문 순서대로 출력한다.
	static int N, M;
	static int[][] map;
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	static boolean[][] visited;
	
	static class Point {
		int x, y;
		Point(int x, int y){
			this.x = x;
			this.y = y;
		}
	}
	
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("./bfs.txt"));
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		visited = new boolean[N][M];
		
		for(int i = 0; i < N; i++) {
			String line = in.readLine();
			for(int j = 0; j < M; j++) {
				map[i][j] = line.charAt(j) - '0';
			}
		}
		
		bfs(0, 0);
		System.out.println(map[N-1][M-1]);
	}
	
	static void bfs(int x, int y) {
		Queue<Point> q = new ArrayDeque<>();
		q.offer(new Point(x, y));
		
		while(!q.isEmpty()) {
			Point cur = q.poll();
			
			
			for(int i = 0; i < 4; i++) {
				int nx = cur.x + dx[i];
				int ny = cur.y + dy[i];
				
				if(nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
				if(visited[nx][ny] == true || map[nx][ny] == 0) continue;
				
				map[nx][ny] = map[cur.x][cur.y] + 1;
				visited[nx][ny] = true;
				q.offer(new Point(nx, ny));
				
			}
		}
		
		
		
	}
	
	static void dfs() {
		
	}

}
