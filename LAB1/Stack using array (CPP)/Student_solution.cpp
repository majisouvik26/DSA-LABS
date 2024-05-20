#include <iostream>
#include <array>

using namespace std;



class Stack {
private:
    int array[200000];
    int head; //indicate the top element
    

public:
    Stack() {
        head = -1;
    }

    void push(int p) {
       array[++head] = p;
    }

    void pop() {
        if ( head==-1 ) {
        cout << "stack is empty" << endl;
        } 
        
        else {
            head--;
        }
    }

    void peek() {
        if ( head==-1 ) {
         cout << -1 <<endl;
        } else {
        cout << array[head] << endl;
        }
    }

    void size() {
        cout << head + 1 <<endl;
    }

    void isempty() {
        if(head==-1){
            cout<<"1"<<endl;
        }
        else{
            cout<<"0"<<endl;
        }
    }
};

int main() {
    Stack stack;
    int m;
    cin >> m;

    while(m--){
        string implement;
        cin >> implement;

     
   if (implement=="push") {
            int z;
            cin >> z;
            stack.push(z);
        } 
        
   else if(implement=="pop") {
            stack.pop();
        } 
        
   else if (implement=="peek") {
            stack.peek();
        } 
        
   else if (implement=="size") {
            stack.size();
        } 
        
   else if (implement=="isempty") {
            stack.isempty();
        }
    }

    return 0;

  }