package heeheejj.swea;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_1225_암호생성기 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        for (int t = 1; t <= 10; t++) {
            in.readLine();
            Queue<Integer> q = new LinkedList<>();
            StringTokenizer st = new StringTokenizer(in.readLine(), " ");

            for(int i = 0; i < 8; i++){
                q.add(Integer.parseInt(st.nextToken()));
            }

            StringBuilder sb = new StringBuilder();
            int divider = 1;
            while(true){
                if(divider > 5){
                    divider = 1;
                }
                int temp = q.poll() - divider;
                if(temp <= 0) {
                    temp = 0;
                    q.add(temp);
                    break;
                }
                q.add(temp);
                divider++;
            }

            System.out.print("#"+t+" ");
            for(int i = 0; i < 8; i++){
                int temp = q.poll();
                sb.append(temp+" ");
            }
            System.out.println(sb);
        }
    }
}