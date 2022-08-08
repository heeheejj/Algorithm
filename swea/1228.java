package heeheejj.swea;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution_1228_암호문1_정희주 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        for (int t = 1; t <= 10; t++) {
            int N = Integer.parseInt(in.readLine());
            ArrayList<Integer> pw = new ArrayList<>();

            // 원본 암호문 입력받아 ArrayList pw에 저장
            StringTokenizer st = new StringTokenizer(in.readLine(), " ");
            for(int i = 0; i < N; i++){
                pw.add(Integer.parseInt(st.nextToken()));
            }

            // 명령어의 개수 입력받기
            int pwN = Integer.parseInt(in.readLine());

            // 명령어를 입력받아 처리
            st = new StringTokenizer(in.readLine(), " ");
            for(int i = 0; i < pwN; i++) {
                if(st.nextToken().equals("I")){
                    int x = Integer.parseInt(st.nextToken());
                    int y = Integer.parseInt(st.nextToken());
                    for(int j = 0; j < y; j++){
                        int temp = Integer.parseInt(st.nextToken());
                        pw.add(x+j, temp);
                    }
                }

            }

            StringBuilder sb = new StringBuilder();
            sb.append("#").append(t).append(" ");
            for(int i = 0; i < 10; i++){
                sb.append(pw.get(i)).append(" ");
            }
            System.out.println(sb);
        }
    }
}
