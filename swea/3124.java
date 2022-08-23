package heeheejj.swea;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_3124_최소스패닝트리_정희주 {
    public static class Edge implements Comparable<Edge> {

        int from, to, weight;

        public Edge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge o) {
            return this.weight - o.weight;
        }
    }

    public static int V, E;
    public static int[] parents;
    public static Edge[] edgeList;

    public static void make() { // 크기가 1인 서로소 집합 생성
        parents = new int[V];
        for (int i = 0; i < V; i++) { // 모든 노드가 자신을 부모로 하는 집합을 생성
            parents[i] = i;
        }
    }

    public static int find(int a) { // a의 대표자 찾는 함수
        if(parents[a] == a)		return a;
        return parents[a] = find(parents[a]); // 경로 압축, 대표자를 나의 부모로 저장
    }

    public static boolean union(int a, int b) { // 리턴값이 true면 union 성공, false면 실패
        int aRoot = find(a);
        int bRoot = find(b);

        if(aRoot == bRoot)	return false;
        parents[bRoot] = aRoot; // rank 관리 안한 코드
        return true; // b의 자식들은 find 함수 실행 시 경로 압축 처리됨
    }

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("./kruskal_input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(in.readLine());
        StringTokenizer st;
        for(int t = 1; t <= T; t++){
            st = new StringTokenizer(in.readLine());

            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            edgeList = new Edge[E];
            parents = new int[V];

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(in.readLine());
                edgeList[i] = new Edge(Integer.parseInt(st.nextToken())-1, // from
                        Integer.parseInt(st.nextToken())-1, // to
                        Integer.parseInt(st.nextToken())); // weight
            }
            make();
            Arrays.sort(edgeList); // 간선들을 오름차순으로 정렬

            long result = 0; // 간선들의 가중치 합
            int count = 0; // 선택한 간선 개수

            for (Edge edge : edgeList) {
                if(union(edge.from, edge.to)) {
                    result += edge.weight;
                    if(++count == V-1)	break;
                }
            }
            sb.append("#").append(t).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
