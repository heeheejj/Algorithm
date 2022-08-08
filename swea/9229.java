package heeheejj.swea;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_9229_한빈이와SpotMart {
    static int N, M;
    static int[] numbers, input;
    static int maxWeight;

    private static void comb(int cnt, int start) {
        if(cnt == 2) {
            int tempWeight = numbers[0] + numbers[1];
            if(tempWeight > M){ // M을 초과하면 바로 return
                return;
            }

            if(maxWeight < tempWeight){
                maxWeight = tempWeight;
            }
            return;
        }

        for(int i = start; i < N; i++) {
            numbers[cnt] = input[i];
            comb(cnt+1, i+1);
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int TC = Integer.parseInt(in.readLine());
        for (int t = 1; t <= TC; t++) {

            StringTokenizer st = new StringTokenizer(in.readLine(), " ");

            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            input = new int[N];
            numbers = new int[2];
            st = new StringTokenizer(in.readLine(), " ");
            for(int i = 0; i < N; i++){
                input[i] = Integer.parseInt(st.nextToken());
            }

            maxWeight = -1;
            comb(0,0);

            StringBuilder sb = new StringBuilder();
            sb.append("#").append(t).append(" ");

            if(maxWeight != -1){
                sb.append(maxWeight);
            }else{
                sb.append(-1);
            }

            System.out.println(sb);
        }
    }
}
