import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1873_상호의배틀필드_정희주 {
    static int H;
    static int W;
    static char[][] map;

    static int nx;  // 전차의 현재 x좌표
    static int ny;  // 전차의 현재 y좌표

    static int dirIdx;  // 전차의 방향 dx, dy를 정하는 idx
                        // 0: 왼쪽, 1:위쪽, 2: 오른쪽, 3: 아래쪽
    static int[] dx = new int[]{0, -1, 0, 1};   // 순서대로 왼쪽, 위쪽, 오른쪽, 아래쪽
    static int[] dy = new int[]{-1, 0, 1, 0};

    static void left(){
        dirIdx = 0;
        int tempNy = ny-1;
        if(tempNy >= 0 && tempNy < W && map[nx][tempNy] == '.') {   // 한 칸 위의 칸이 평지라면
            map[nx][ny] = '.';  // 기존의 자리는 평지가 된다.
            ny -= 1;    // 전차 위치 이동
        }
        map[nx][ny] = '<';
    }

    static void up(){
        dirIdx = 1;
        int tempNx = nx-1;
        if(tempNx >= 0 && tempNx < H && map[tempNx][ny] == '.'){    // 한 칸 위의 칸이 평지라면
            map[nx][ny] = '.';  // 기존의 자리는 평지가 된다.
            nx -= 1;    // 전차 위치 이동
        }
        map[nx][ny] = '^';
    }

    static void right(){
        dirIdx = 2;
        int tempNy = ny+1;
        if(tempNy >= 0 && tempNy < W && map[nx][tempNy] == '.'){    // 한 칸 위의 칸이 평지라면
            map[nx][ny] = '.';  // 기존의 자리는 평지가 된다.
            ny += 1;    // 전차 위치 이동
        }
        map[nx][ny] = '>';
    }

    static void down(){
        dirIdx = 3;
        int tempNx = nx+1;
        if(tempNx >= 0 && tempNx < H && map[tempNx][ny] == '.') {   // 한 칸 위의 칸이 평지라면
            map[nx][ny] = '.';  // 기존의 자리는 평지가 된다.
            nx += 1;    // 전차 위치 이동
        }
        map[nx][ny] = 'v';
    }

    static void shoot(){
        int tx = nx + dx[dirIdx];
        int ty = ny + dy[dirIdx];
        // 벽돌벽에 충돌 or 강철벽에 충돌 or 범위 벗어날때까지 반복
        // == (!벽돌벽에 충돌 and !강철벽에 충돌 and !범위 벗어날)때까지 반복
        // == (!벽돌벽에 충돌 and !강철벽에 충돌 and 올바른 범위일)때까지 반복
        while(tx >= 0 && tx < H && ty >= 0 && ty < W){
            char tempChar = map[tx][ty];
            if(tempChar == '*') {   // 벽돌벽에 부딪히면 벽돌벽 위치가 평지가 됨
                map[tx][ty] = '.';
                break;
            } else if(tempChar == '#'){ // 강철벽에 부딪히면 아무일도 일어나지 않고 종료
                break;
            }
            tx += dx[dirIdx];
            ty += dy[dirIdx];
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));	// . = 현재 디렉토리 = 프로젝트 바로 밑 (input1.txt가 프로젝트 바로 밑에 있음)

        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(in.readLine());

        for (int t = 1; t <= TC; t++) {
            StringTokenizer st = new StringTokenizer(in.readLine(), " ");
            H = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());

            dirIdx = -1;    // 테스트케이스마다 전차의 방향 초기화
            nx = -1;        // 전차의 x좌표 초기화
            ny = -1;        // 전차의 y좌표 초기화

            // 게임 맵의 구성요소를 2차원배열로 저장
            map = new char[H][];
            for(int i = 0; i < H; i++){
                char[] temp = in.readLine().toCharArray();
                map[i] = temp;
                for(int j = 0; j < W; j++){ // 전차 위치 확인
                    char tempChar = temp[j];
                    if(tempChar == '<'){
                        dirIdx = 0;
                        nx = i; ny = j;
                        break;
                    } else if(tempChar == '^'){
                        dirIdx = 1;
                        nx = i; ny = j;
                        break;
                    } else if(tempChar == '>'){
                        dirIdx = 2;
                        nx = i; ny = j;
                        break;
                    } else if(tempChar == 'v'){
                        dirIdx = 3;
                        nx = i; ny = j;
                        break;
                    }
                }
            }

            // 사용자의 입력에 따라, 해당 동작을 하는 함수 호출
            int N = Integer.parseInt(in.readLine());
            char[] inputs = in.readLine().toCharArray();

            for(char c: inputs){
                if(c == 'L'){
                    left();
                } else if(c == 'U'){
                    up();
                } else if(c == 'R'){
                    right();
                } else if(c == 'D'){
                    down();
                } else if(c == 'S'){
                    shoot();
                }
            }

            System.out.print("#"+t+" ");
            for(int i = 0; i < H; i++){
                for(int j = 0; j < W; j++){
                    System.out.print(map[i][j]);
                }
                System.out.println();
            }
        }
    }
}
