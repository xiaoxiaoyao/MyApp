package main.java;

public final class thirteen {
	public static void main(String[] args) {
		int tri=0;
		triLoop:
			while(tri<400) {
				tri++;
				if (tri % 13 == 0) {
					System.out.println(tri);
					continue triLoop;
				}
				System.out.print('N');
			}
	}

}
