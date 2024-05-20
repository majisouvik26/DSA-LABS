#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <regex>


using namespace std;

class PhoneRecord { 
    
private:

    string name;
    string organisation;
    vector<string> phoneNumbers;

public:

    PhoneRecord(const string& n, const string& org, const vector<string>& numbers)
        : name(n), organisation(org), phoneNumbers(numbers) {}

    // Getters for name, organisation, and phoneNumbers

    string getName() const {
        return name;
    }

    string getOrganisation() const {
        return organisation;
    }

    vector<string> getPhoneNumbers() const {
        return phoneNumbers;
    }
};

class HashTableRecord {
private:
    int key;
    PhoneRecord* record;
    HashTableRecord* next;

public:
    HashTableRecord(int k, PhoneRecord* r) : key(k), record(r), next(nullptr) {}
    
    // Getters and setters for key, record, and next

    int getKey() const {
        return key;
    }

    PhoneRecord* getRecord() const {
        return record;
    }

    HashTableRecord* getNext() const {
        return next;
    }

    void setNext(HashTableRecord* n) {
        next = n;
    }
};

class PhoneBook {
    
private:

    static const int HASH_TABLE_SIZE = 263; // Fixed size of the hash table
    HashTableRecord* hashTable[HASH_TABLE_SIZE];

public:

    PhoneBook() {
        // Initialize the hash table slots to nullptr
        for (int i = 0; i < HASH_TABLE_SIZE; ++i) {
            hashTable[i] = nullptr;
        }
    }

    // Function to compute the hash value for a given string
    long long computeHash(const string& str) const {
        const long long int p = 1000000007;
        const long long int x = 263;
        const long long int m = HASH_TABLE_SIZE;
        long long int power_x = 1;
        long long int hashValue = 0;

        for (char c : str) {
            hashValue = (hashValue + (c * power_x) % p) % m;
            power_x = (power_x * x) % p;
        }

        return hashValue;
    }
    
    // Implement methods for adding, deleting, and fetching contacts

    void addContact(PhoneRecord* record) {
        // Implement adding a contact to the phone book
        string name = record->getName();

        vector<string> words = split_name(name);

        for (const string& word : words) {
            int key = computeHash(word);
            HashTableRecord* flag = new HashTableRecord(key, record);

            if (hashTable[key] == nullptr) {
                hashTable[key] = flag;
            } 
            else {
                
                HashTableRecord* temp = hashTable[key];
                while (temp->getNext() != nullptr) {
                    temp = temp->getNext();
                    
                }
                
                temp->setNext(flag);
            }
        }
    }

    vector<PhoneRecord*> fetchContacts(const string* query) {
     // Implement fetching contacts based on the query
     // You may need to split the query into words and hash them separately
     // Then, retrieve and merge the records from the appropriate hash table slots
     // Sort and return the merged records
     
     unordered_map<PhoneRecord*, int> c;  //c records the count // unordered map approach

     vector<string> words = split_name(*query);
     for (const string& word : words) {
        int key = computeHash(word);
        HashTableRecord* current = hashTable[key]; 
        
        while (current) {
            PhoneRecord* record = current->getRecord();
            if (c.find(record) == c.end()) {
                c[record] = 1;
            } else {
                c[record] = c[record] + 1 ;
            }
            current = current->getNext();
        }
    }

    vector<pair<PhoneRecord*, int>> sort_record(c.begin(), c.end());
    
    sort(sort_record.begin(), sort_record.end(),
         [](const pair<PhoneRecord*, int>& a, const pair<PhoneRecord*, int>& b) {
             return a.second > b.second;
         });

    vector<PhoneRecord*> v;
    for (const auto& pair : sort_record) {
        v.push_back(pair.first);
    }

    return v;
 }

    bool deleteContact(const string* search_name) { 
        
    // Implement deleting a contact from the phone book
    
    string name = *search_name;
    vector<PhoneRecord*> contacts = fetchContacts(&name);

    if (contacts.empty())
        return false;

    // Iteration process
    for (PhoneRecord* contact : contacts) {
        for (const string& word : split_name(contact->getName())) {
            int key = computeHash(word);
            HashTableRecord* current = hashTable[key];
            HashTableRecord* previous = nullptr;

            while (current && current->getRecord() != contact) {
                previous = current;
                current = current->getNext();
            }

            if (current) {
                if (previous)
                    previous->setNext(current->getNext());
                else
                    hashTable[key] = current->getNext();

                delete current;
            }
        }
    }

    return true;
}


    // defining split_name function
    vector<string> split_name(const string& record) const {
        vector<string> words;
        stringstream ss(record);
        string word;
        // it will split names from white spaces like "Sachin Tendulkar" to "Sachin" and "Tendulkar"
        while (ss >> word) {
            words.push_back(word);
        }

        return words;
    }
    
    //defining readRecordsFromFile to read the input file 

    void readRecordsFromFile(const string& filename) {
    ifstream inputFile(filename);
    string line;
    //string mainline;

    // Defining the pattern
    regex pattern(R"(([^,]+)(,[^,]+)+,([^,]+))");

    while (getline(inputFile, line)) {
        //cout << line << endl;
        //string line = mainline;
        smatch components;

        // Sequencing objects of txt file
        while (regex_search(line, components, pattern)) {
            string name = components[1];
            vector<string> phone_numbers;

            // phone numbers may be one,two or more than two 
            /*for (size_t i = 2; i < components.size(); ++i) {
                phone_numbers.push_back(components[i]);
            }*/
            for (size_t i = 2; i < components.size() - 1; ++i) {
                phone_numbers.push_back(components[i]);
            }
            
            string organisation = components[components.size() - 1];

            // Dynamic allocation of PhoneRecord
            
            //PhoneRecord* record = new PhoneRecord(name, phone_numbers, organisation);
            PhoneRecord* record = new PhoneRecord(name, organisation, phone_numbers);
            
            // Adding this record using function
            addContact(record);

            line = components.suffix();
        }
        //cout << mainline << endl;
        //cout<<line<<endl;
     }

    inputFile.close();
   
    }
    
    int countRecordsPointingTo(const PhoneRecord* record) {
    int count = 0;

    for (int i = 0; i < HASH_TABLE_SIZE; ++i) {
        HashTableRecord* temp = hashTable[i];

        while (temp) {
            if (temp->getRecord() == record) {
               // cout << record->getName() << endl;
                ++count;
            }
            temp = temp->getNext();
        }
    }

    return count;
}


    
};

/*vector<string> split_name(const string& record);

int main() {
    string name = "Souvik Maji";
    vector<string> names = split_name(name);

    for (const string& part : names) {
        cout << part << " "<<endl;
    }

    return 0;
}

vector<string> split_name(const string& record) {
    vector<string> words;
    stringstream ss(record);
    string word;
    while (ss >> word) {
        words.push_back(word);
    }
    return words;
}*/
