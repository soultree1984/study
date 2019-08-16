import java.util.Scanner;

//https://codeup.kr/problem.php?id=1099
//1099 : [기초-종합+배열] 성실한 개미
public class CodeUp1099 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int h = 10;
        int w = 10;

        String[] str = new String[h];
        for(int i = 0 ; i < h ; i ++){
            str[i] = sc.nextLine();
        }

        int[][] mazeBox = new int[h][w];

        for(int t = 0 ; t < str.length ; t++){
            String[] widthArr = str[t].split(" ");
            for(int j = 0; j < widthArr.length ; j++){
                int width = Integer.parseInt(widthArr[j]);
                mazeBox[t][j] = width;
            }
        }

        int x = 1; //시작위치
        int y = 1; //시작위치

        mazeBox[1][1] = 9; //시작위치

        boolean isFinished = false;

        while(!isFinished){

            if(mazeBox[y][x+1] == 1){ //오른쪽이 막힌 경우
                if(mazeBox[y+1][x] == 1){ // 아래가 막힌 경우
                    isFinished = true; //오른쪽 아래쪽 모두 막혀서 갈곳 없음.
                }else{
                    y++; //아래쪽 길이 있음
                }
            }else if(mazeBox[y][x+1] != 1){ // 오른쪽 길이 있음
                x++;
            }

            if(mazeBox[y][x] == 2){ //먹이를 먹었을 경우
                isFinished = true;
            }

            mazeBox[y][x] = 9; // 경로 표시
        }

        //maze box 출력.
        for(int i = 0 ; i < h ; i++){
            for(int j = 0 ; j < w ; j++){
                System.out.print(mazeBox[i][j]+" ");
            }
            System.out.println("");
        }
    }
}
