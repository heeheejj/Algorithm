package heeheejj.swea;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_5215_햄버거다이어트_정희주 {
    static int score_max;
    static int N, L;
    static int[][] inputs;

    static void check(int idx, int score, int cal){
        if(cal > L) return;
        if(score > score_max) score_max = score;
        if(idx == N) return;

        check(idx+1, score, cal);
        check(idx+1, score+inputs[idx][0], cal + inputs[idx][1]);
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(in.readLine());

        StringBuilder sb = new StringBuilder();
        for (int t = 1; t <= TC; t++) {

            StringTokenizer st = new StringTokenizer(in.readLine(), " ");
            N = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());

            inputs = new int[N][2];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(in.readLine(), " ");
                inputs[i][0] = Integer.parseInt(st.nextToken());
                inputs[i][1] = Integer.parseInt(st.nextToken());
            }

            score_max = 0;
            check(0, 0, 0);

            sb.append("#").append(t).append(" ").append(score_max).append("\n");
        }
        System.out.print(sb);
    }
}
