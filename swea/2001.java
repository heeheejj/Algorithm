package heeheejj.swea;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 누적합(Prefix Sum)으c로 풀기
public class Solution_2001_파리퇴치_정희주 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(in.readLine());

        for (int t = 1; t <= TC; t++) {
            StringTokenizer st = new StringTokenizer(in.readLine(), " ");
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int[][] map = new int[N+1][N+1];
            int[][] dp = map; // dp[n][k]는 (0,0)부터 (n,k)까지의 합
            for(int n = 1; n <= N; n++){
                st = new StringTokenizer(in.readLine(), " ");
                for(int k = 1; k <= N; k++){
                    map[n][k] = Integer.parseInt(st.nextToken());
                }

                for(int k = 1; k <= N; k++){
                    dp[n][k] = dp[n-1][k] + dp[n][k-1] - dp[n-1][k-1] + map[n][k];
                }
            }

            int maxSum = Integer.MIN_VALUE;
            for(int n = M; n <= N; n++){
                for(int k = M; k <= N; k++){
                    int sum = dp[n][k] - dp[n-M][k] - dp[n][k-M] + dp[n-M][k-M];
                    if(sum > maxSum){
                        maxSum = sum;
                    }
                }
            }
            System.out.println("#" + t + " " + maxSum);
        }
    }
}
