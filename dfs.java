package bfs_dfs;

import java.util.Scanner;
// https://www.acmicpc.net/problem/4963 섬의 개수
public class DfsTest {
	static int W; // 지도의 너비
	static int H; // 지도의 높이
	static int[][] Map; // 지도 2차원 배열
	static int[] dx = {0, 0, 1, -1, -1, 1, -1, 1};
	static int[] dy = {1, -1, 0, 0, -1, 1, 1, -1};
	static boolean[][] check; //방문 여부
 	static int count; //섬의 갯수

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true) {
			W = sc.nextInt(); // 지도의 너비
			H = sc.nextInt(); // 지도의 높이
			
			//0 0이 입력되면 종료
			if(W==0 && H==0) System.exit(0);
			
			//지도 2차원 배열선언
			Map = new int[H][W];
			
			//좌표 방문 체크
			check = new boolean[H][W];
			
			//지도 2차원 배열 입력
			for(int i=0;i<H;i++) {
				for(int j=0;j<W;j++) {
					Map[i][j] = sc.nextInt(); 
				}
			}
			
			count = 0;
			
			
			for(int i=0;i<H;i++) {
				for(int j=0;j<W;j++) {
					//Search에 들어가면 count 증가
					if(Map[i][j]==1 && !check[i][j]) {
						Search(i,j);
						count++;
					}
				}
			}
			//섬의 갯수 출력
			System.out.println(count);
		}
		
		
	}
	
	public static void Search(int x, int y) {
		check[x][y] = true;
		
		//8방향 확인
		for(int i=0;i<8;i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			
			//범위 안에 있고 배열 값이 1이고 true라면
			if(nx>=0 && ny>=0 && nx<H && ny<W) {
				if(Map[nx][ny]==1 && !check[nx][ny]) Search(nx,ny);
			}
		}
	}

}
