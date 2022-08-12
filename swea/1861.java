package heeheejj.swea;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_1861_정사각형방_정희주 {
    static int[][] map;
    static int N;
    static int cnt;

    public static int dfs(int x, int y){    // 방 개수를 리턴

        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        int nx = x;
        int ny = y;
        for(int i = 0; i < 4; i++){
            int tempX = nx + dx[i];
            int tempY = ny + dy[i];

            if(tempX < 0 || tempX >= N || tempY < 0 || tempY >= N){
                continue;
            }

            if(map[tempX][tempY] == map[x][y] + 1){
                cnt++;
//                System.out.println("cnt: "+cnt+"/ tempX: "+tempX+"/ tempY: "+tempY);
                dfs(tempX, tempY);
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int TC = Integer.parseInt(in.readLine());

        for (int t = 1; t <= TC; t++) {
            N = Integer.parseInt(in.readLine());
            map = new int[N][N];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(in.readLine(), " ");
                for (int j = 0; j < N; j++) {
                    int temp = Integer.parseInt(st.nextToken());
                    map[i][j] = temp;
                }
            }

            int maxCnt = 0;

            int resultNum = Integer.MAX_VALUE;
            for(int i = 0; i < N; i++){
                for (int j = 0; j < N; j++) {
                    cnt = 1;
                    dfs(i, j);
                    // dfs 탐색 끝나면 처음 출발하는 방 번호와 방 개수 구하기
                    // 방 개수가 max방개수보다 많다면 갱신, 처음 출발하는 방 번호 바꿔치기
                    int tempNum = map[i][j];
//                    System.out.println("tempNum: "+tempNum);
                    if(maxCnt < cnt){
                        maxCnt = cnt;
//                        System.out.println("resultNum: "+resultNum+"/ map[i][j]: "+map[i][j]);
                        resultNum = tempNum;
//                        System.out.println("startPoint: i: "+i+" j: "+j+" 갱신된 maxCnt: "+maxCnt);
                    } else if(maxCnt == cnt){
                        // 최대인 값이 여럿이라면 그 중에서 적힌 수가 가장 작은 수로 갱신
                        // 최대인 값이 또 나오면 적힌 수가 더 작을 때만 갱신
                        if(resultNum > map[i][j]){
//                            System.out.println("resultNum: "+resultNum+"/ map[i][j]: "+map[i][j]);
                            resultNum = tempNum;
//                            System.out.println("startPoint: i: "+i+" j: "+j+"maxCnt 그대로: "+maxCnt);
                        }
                    }
                }
            }
            sb.append("#").append(t).append(" ");
            // startPoint와 방 개수 구하고 출력
            sb.append(resultNum).append(" ").append(maxCnt).append("\n");
        }
        System.out.println(sb);
    }
}