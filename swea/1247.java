package heeheejj.swea;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1247_최적경로_정희주 {
// 가중치가 있으니까 DFS?
    static int N;
    static int[][] clientPos;
    static int homeX, homeY;
    static boolean[] isSelected;
    static int minDist;

    static int getDist(int x1, int y1, int x2, int y2){
        return Math.abs(x1-x2)+Math.abs(y1-y2);
    }

    static void dfs(int cnt, int x, int y, int dist){   // x, y: 현재 위치, dist: 현재까지 거리
        if(cnt == N){
            dist += getDist(x, y, homeX, homeY); // 집까지의 거리 dist에 더하기
            if(minDist > dist){ // minDist보다 작으면 갱신
                minDist = dist;
            }
            return;
        }

        for(int i = 0; i < N; i++){
            if(!isSelected[i]){ // 방문한 적 없으면
                isSelected[i] = true;
                int clientX = clientPos[i][0];  int clientY = clientPos[i][1];
                dfs(cnt+1, clientX, clientY, dist + getDist(x, y, clientX, clientY));
                isSelected[i] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int TC = Integer.parseInt(in.readLine());

        for (int t = 1; t <= TC; t++) {
            N = Integer.parseInt(in.readLine());
            StringTokenizer st = new StringTokenizer(in.readLine(), " ");
            int officeX = Integer.parseInt(st.nextToken()); int officeY = Integer.parseInt(st.nextToken());
            homeX = Integer.parseInt(st.nextToken());   homeY = Integer.parseInt(st.nextToken());
            clientPos = new int[N][2];
            isSelected = new boolean[N];
            minDist = Integer.MAX_VALUE;
            for (int i = 0; i < N; i++) {
                clientPos[i][0] = Integer.parseInt(st.nextToken());
                clientPos[i][1] = Integer.parseInt(st.nextToken());
            }

            dfs(0, officeX, officeY, 0);
            sb.append("#").append(t).append(" ").append(minDist).append("\n");
        }
        System.out.print(sb);
    }
}