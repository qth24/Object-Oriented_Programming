#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string id, name, gender;
    int birthYear;
    float gpa;

public:
    void input() {
        cout << "Enter ID: ";
        getline(cin, id);
        cout << "Enter name: ";
        getline(cin, name);
        cout << "Enter gender: ";
        getline(cin, gender);
        cout << "Enter birth year: ";
        cin >> birthYear;
        cout << "Enter GPA: ";
        cin >> gpa;
        cin.ignore(); // discard newline
    }

    void display() {
        cout << name << " (ID: " << id 
             << ", Birth Year: " << birthYear 
             << ", GPA: " << gpa << ")\n";
    }

    float getGPA() { return gpa; }
    int getBirthYear() { return birthYear; }
    string getName() { return name; }
};

int main() {
    Student s1, s2;

    cout << "- Enter information for student 1:\n";
    s1.input();
    cout << "- Enter information for student 2:\n";
    s2.input();

    if (s1.getGPA() > s2.getGPA())
        cout << "\n> Student with higher GPA: " << s1.getName() << endl;
    else if (s1.getGPA() < s2.getGPA())
        cout << "\n> Student with higher GPA: " << s2.getName() << endl;
    else
        cout << "\n> Both students have the same GPA\n";

    if (s1.getBirthYear() > s2.getBirthYear())
        cout << "> Younger student: " << s1.getName() << endl;
    else if (s1.getBirthYear() < s2.getBirthYear())
        cout << "> Younger student: " << s2.getName() << endl;
    else
        cout << "> Both students are the same age\n";

    return 0;
}
