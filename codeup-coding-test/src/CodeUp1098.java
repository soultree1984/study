import java.util.Scanner;

//https://codeup.kr/showsource.php?id=10072098
//1098 : [기초-종합+배열] 설탕과자 뽑기
public class CodeUp1098 {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        String[] wXh= sc.nextLine().split(" ");

        int w = Integer.parseInt(wXh[1]); //가로
        int h = Integer.parseInt(wXh[0]); //세로
        int n = Integer.parseInt(sc.nextLine()); //막대 개수

        String[] stickArray = new String[n];
        for(int i = 0 ; i < n ; i++){
            stickArray[i] = sc.nextLine();
        }

        /*
        stickArray[0] = "2 0 1 1";
        stickArray[1] = "3 1 2 3";
        stickArray[2] = "4 1 2 5";
        */
        int[][] board = new int[h][w];

        //보드 0으로 초기화
        for(int i = 0 ; i < h ; i++){
            for(int j = 0 ; j < w ; j++){
                board[i][j] = 0;
            }
        }

        int[][] stick = new int[n][4];

        for(int i = 0 ; i < n ; i ++){
            String[] temp = stickArray[i].split(" ");
            for(int j = 0 ; j < temp.length ; j++){
                stick[i][j] = Integer.parseInt(temp[j]);
            }
        }

        //Stick 출력
        for(int i = 0 ; i < n ; i++){

            int l = stick[i][0];
            int d = stick[i][1];
            int x = stick[i][3] - 1; //0 부터 시작
            int y = stick[i][2] - 1; //0 부터 시작

            //가로 >
            if(d == 0){
                for(int j = 0 ; j < l; j++){
                    board[y][x+j] = 1;
                }
            }
            //세로 V
            else{
                for(int j = 0 ; j < l; j++){
                    board[y+j][x] = 1;
                }
            }
        }

        //보드 출력
        for(int i = 0 ; i < h ; i++){

            for(int j = 0 ; j < w ; j++){
                System.out.print(board[i][j]+ " ");
            }
            System.out.println("");
        }

    }
}
