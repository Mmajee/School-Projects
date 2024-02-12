package cp213;

import java.util.Scanner;

public class Movie {
	
	
	private final int FIRST_YEAR = 1800;
	private final String[] GENRES = {"science fiction", "fantasy", "drama", "romance", "comedy", "zombie", "action", "historical", "horor", "war"};
	
	private final Double MAX_RATING = 10.0;
	private final Double MIN_RATING = 0.0;
	
	private String title = "";
	private String director = "";
	private int year = 0;
	private int genre = 0;
	private Double rating = 0.0;
	
	
	public static void main(String[] args) {
		
		Movie obj1 = new Movie();
		
		int comparison = 0;
		
		Movie obj2 = new Movie("Dellamorte Dellamore", "Michele Soavi", 1994, 3, 7.2);
		Movie obj3 = new Movie("Zulu", "Jerome Salle", 2013, 2, 6.7);
		
		System.out.println();
		
		String movieString = obj1.toString();
		String movieString2 = obj2.toString();
		String movieString3 = obj3.toString();
		
		System.out.println(movieString);
		System.out.println();
		System.out.println(movieString2);
		System.out.println();
		System.out.println(movieString3);
		
		System.out.println();
		
		comparison = obj1.compareTo(obj1);
		System.out.println(comparison);
		System.out.println();
		
		comparison = obj3.compareTo(obj1);
		System.out.println(comparison);
		System.out.println();
		
		comparison = obj1.compareTo(obj2);
		System.out.println(comparison);
		
		
			
	}
	
	public String getTitle() {
		return this.title;
		
	}
	
	public String getDirector() {
		return this.director;
	}
	
	public int getYear() {
		return this.year;
	}
	
	public int getGenre() {
		return this.genre;
	}
	
	public Double getRating() {
		return this.rating;
	}
	
	public void setTitle(final String arg) {
		this.title = arg;
	}
	
	public void setDirector(final String arg) {
		this.director = arg;
	}
	
	public void setYear(final int arg) {
		this.year = arg;
	}
	
	public void setGenre(final int arg) {
		this.genre = arg;
	}
	
	public void setRating(final double arg) {
		this.rating = arg;	
	}
	
	public String genreToName(int genNum) {
		String genreName = "";
		
		genreName = GENRES[genNum];
		
		return genreName ;
	}
	
	public String genreMenue() {
		String List = "";
		
		for (int i = 0; i < GENRES.length; i++) {
			
			List = List + String.valueOf(i) + ": " + GENRES[i] + "\n";
		}
		return List;
	}
	
	public String toString() {
		String movieString = "";
		String genreString = "";
		
		genreString = genreToName(getGenre());
		
		
		movieString = "Title: " + getTitle() + "\n" +
						"Year: " + String.valueOf(getYear()) + "\n" + 
						"Director: " + getDirector() + "\n" + 
						"Rating: " + String.valueOf(getRating()) + "\n" + 
						"Genre: " + genreString;
		
		return movieString;
	}
	
	public int compareTo(Movie obj) {
		int result = 0;
		
		
		if (this.title.equals(obj.title) & this.year == obj.year & this.director.equals(obj.director) & this.rating == obj.rating & this.genre == obj.genre) {
			result = 0;
		}
		else if (this.year == obj.year) {
			result = this.FIRST_YEAR;
		}
		else {
			result = this.year - obj.year;
		}	
		
		return result;
	}
	
	Movie() {
		Scanner keyboard = new Scanner(System.in);
		
		String title = "";
		String director = "";
		int year = 0;
		int genreNum = -1;
		Double rating = -1.0;
		
		String List = "";
		
		System.out.print("Title: ");
		title = keyboard.nextLine();
		setTitle(title);
		
		while (year < FIRST_YEAR) {	
			System.out.print("Year: ");
			year = keyboard.nextInt();
			}
		setYear(year);
		
		System.out.print("Director: ");
		director = keyboard.nextLine();
		director = keyboard.nextLine();
		setDirector(director);
		
		while (rating < MIN_RATING | rating > MAX_RATING) {
			System.out.print("Rating: ");
			rating = keyboard.nextDouble();
		}
		setRating(rating);
		
		while (genreNum < 0 | genreNum > 9) {
			System.out.println("Genre: ");
			List = genreMenue();
			System.out.println(List);
			genreNum = keyboard.nextInt();
		}
		setGenre(genreNum);
		
		keyboard.close();
		
	}
	
	Movie(String arg1, String arg2, int arg3, int arg4, Double arg5) {
		
		setTitle(arg1);
		setDirector(arg2);
		setYear(arg3);
		setGenre(arg4);
		setRating(arg5);

	}
	
}
