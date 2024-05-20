#include<bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <map>
using namespace std;



// Forward declarations
class MetroStop;
class MetroLine;
class AVLNode;

// MetroStop class
class MetroStop {
private:
    std::string stopName;
    MetroStop* nextStop;
    MetroStop* prevStop;
    MetroLine* line;
    int fare;

public:
    MetroStop(std::string name, MetroLine* metroLine, int fare){
        stopName = name;
        line = metroLine;
        this-> fare = fare;
        nextStop = NULL;
        prevStop = NULL;
    }

    // Getter methods
    std::string getStopName() const{
        return stopName;
    }
    MetroStop* getNextStop() const{
        return nextStop;
    }
    MetroStop* getPrevStop() const{
        return prevStop;
    }
    MetroLine* getLine() const{
        return line;
    }
    int getFare() const{
        return fare;
    }

    // Setter methods
    void setNextStop(MetroStop* next){
        this-> nextStop = next;
    }
    void setPrevStop(MetroStop* prev){
        this-> prevStop = prev;
    }
};

#include <vector>
#include <string>

std::vector<std::string> tokenizeSubstring(const std::string& substring) {
    std::vector<std::string> tokens;
    std::string token;
    for (char c : substring) {
        if (c == ' ') {
            token += ' ';
            tokens.push_back(token);
            token = "";
        } else {
            token += c;
        }
    }
    return tokens;
}

std::vector<std::string> breakline(const std::string& line) {
    std::vector<std::string> my;
    std::string subline;
    std::string subline2;

    for (int i = 0; i < line.size(); ++i) {
        if (line[i] == ' ') {
            subline += ' ';
            std::vector<std::string> tokens = tokenizeSubstring(subline);
            my.insert(my.end(), tokens.begin(), tokens.end());
            subline = "";
        } else {
            subline = subline + line[i];
        }
    }

    for (int i = 0; i < subline.size(); ++i) {
        if (subline[i] == ',') {
            break;
        }
        subline2 = subline2 + subline[i];
    }

    my.push_back(subline2);

    return my;
}


vector<string> details;



vector<MetroStop* > make_stops_list(vector<string> details, vector<MetroStop* > stopslist, int ffare, MetroLine* lineaddress){
    
    string stpname = "";
    string stpname2 = "";
    for(int i = 0 ; i<details.size()-1 ; i++){
        stpname = stpname + details[i];
       
    }
    
    for(int i = 0 ; i<stpname.size()-1 ; i++){
        stpname2 = stpname2 + stpname[i];
    }
   
    MetroStop* temp = new MetroStop(stpname2, lineaddress , ffare);
    
    stopslist.push_back(temp);
    return stopslist;
}

vector<MetroStop*> connectlist(vector<MetroStop*> stopslist){
    for(int i = 0 ; i<stopslist.size()-1 ; i++){
        stopslist[i]-> setNextStop(stopslist[i+1]) ;
        stopslist[i+1]-> setPrevStop(stopslist[i]) ;
    }
    return stopslist;
}


class MetroLine {
private:
    std::string lineName;
    MetroStop* node;
    vector<MetroStop*> stopslist;

public:
    MetroLine(std::string name){
        lineName = name;
    }

    // Getter methods
    std::string getLineName() {
        return lineName;
    }
    MetroStop* getNode() {
        return this-> node;
    }

    // Setter methods
    void setNode(MetroStop* node){
        this-> node = node;
    }

   void populateLine(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        // Handle file opening error
        return;
    }

    std::string line;
    int num = 1;
    int prevFare;
    int currFare = 0;
    int finalFare;

    while (std::getline(file, line)) {
        details = breakline(line);

        prevFare = currFare;
        currFare = 0;

        // Convert string to integer using a loop
        for (char digit : details[details.size() - 1]) {
            if (isdigit(digit)) {
                currFare = currFare * 10 + (digit - '0');
            } else {
                // Handle non-digit characters if necessary
            }
        }

        finalFare = currFare - prevFare;

        stopslist = make_stops_list(details, stopslist, finalFare, this);
    }

    stopslist = connectlist(stopslist);
    setNode(stopslist[0]);
}


    // helper function
    void printLine(std::ostream& output = std::cout) const {
    for (int i = 0; i < stopslist.size(); i++) {
        output << stopslist[i]->getStopName() << std::endl;
    }
}
    int getTotalStops() {
        
        return stopslist.size();
    }
};

vector<MetroLine*> lines;

class AVLNode {
private:
    std::string stopName;
    std::vector<MetroStop*> stops;
    AVLNode* left;
    AVLNode* right;
    AVLNode* parent;

public:
    AVLNode(std::string name);

    // Getter methods
    std::string getStopName() const;
    const std::vector<MetroStop*>& getStops() const;
    AVLNode* getLeft() const;
    AVLNode* getRight() const;
    AVLNode* getParent() const;

    // Setter methods
    void addMetroStop(MetroStop* metroStop);
    void setLeft(AVLNode* left);
    void setRight(AVLNode* right);
    void setParent(AVLNode* parent);
};

AVLNode::AVLNode(std::string name) {
    stopName = name;
    left = NULL;
    right = NULL;
}

std::string AVLNode::getStopName() const {
    return stopName;
}

const std::vector<MetroStop*>& AVLNode::getStops() const {
    return stops;
}

AVLNode* AVLNode::getLeft() const {
    return left;
}

AVLNode* AVLNode::getRight() const {
    return right;
}

AVLNode* AVLNode::getParent() const {
    return parent;
}

void AVLNode::setLeft(AVLNode* left) {
    this->left = left;
}

void AVLNode::setRight(AVLNode* right) {
    this->right = right;
}

void AVLNode::setParent(AVLNode* parent) {
    this->parent = parent;
}

void AVLNode::addMetroStop(MetroStop* metroStop) {
    stops.push_back(metroStop);
}


int max(int x, int y) {
    return (x > y) ? x : ((x <= y) ? y : 0);
}


// AVLTree class
class AVLTree {
    
private:
    AVLNode* root;

public:
    // getter methods
    AVLNode* getRoot() const;

    // setter methods
    void setRoot(AVLNode* root);

    // helper functions
    int height(AVLNode* node);
    int balanceFactor(AVLNode* node);
    AVLNode* rotateLeft(AVLNode* node);
    AVLNode* rotateRight(AVLNode* node);
    void balance(AVLNode* node);
    int stringCompare(string s1, string s2);
    AVLNode* insert(AVLNode* node, MetroStop* metroStop);
    void populateTree(MetroLine* metroLine);
    void inOrderTraversal(AVLNode* node);
    int getTotalNodes(AVLNode* node);
    AVLNode* searchStop(string stopName);
    void printTree(AVLNode* node, int level = 0);
    bool isTreeBalanced(AVLNode* node);
    void printNodeDetails(AVLNode* node);
};


AVLNode* AVLTree::getRoot() const {
    return root;
}

void AVLTree::setRoot(AVLNode* root) {
    this->root = root;
}

int AVLTree::height(AVLNode* node) {
    if(node == NULL){
        return 0 ;
    }
    int leftheight = height(node->getLeft());
    int rightheight = height(node->getRight());
    return max(leftheight,rightheight) + 1;
    
}

int AVLTree::stringCompare(string s1, string s2) {
    // use strcmp

    char *c1 = new char[s1.length() + 1];
    strcpy(c1, s1.c_str());

    char *c2 = new char[s2.length() + 1];
    strcpy(c2, s2.c_str());

    int result = strcmp(c1, c2);
    return result;
}





int AVLTree::balanceFactor(AVLNode* node) {
    
   
    return height(node->getLeft()) - height(node->getRight()) ;
   
}

AVLNode* AVLTree::rotateLeft(AVLNode* node) {
    AVLNode*y = node->getRight();
	AVLNode*x = y->getLeft();

	// Perform rotation
	y->setLeft(node) ;
	node->setRight(x) ;

	
    return y;

}

AVLNode* AVLTree::rotateRight(AVLNode* node) {
    AVLNode* x = node->getLeft();
	AVLNode* y = x->getRight();

	// Perform rotation
	x->setRight(node) ;
	node->setLeft(y) ;


    return x;
}

int computeLexiOrder(string s1, string s2){
    return s1.compare(s2);
}

void AVLTree::balance(AVLNode* node) {
}

bool isOrderLessThanZero(const std::string& stopName1, const std::string& stopName2) {
    return computeLexiOrder(stopName1, stopName2) < 0;
}
bool isOrderGreaterThanZero(const std::string& stopName1, const std::string& stopName2) {
    return computeLexiOrder(stopName1, stopName2) > 0;
}

AVLNode* AVLTree::insert(AVLNode* node, MetroStop* metroStop) {
    if (node == nullptr){
        
		AVLNode* temp = new AVLNode(metroStop->getStopName());
        temp->addMetroStop(metroStop);
        return temp;
    }
    
	if (isOrderLessThanZero(metroStop->getStopName(), node->getStopName())) {
        node->setLeft(insert(node->getLeft(), metroStop));
    } else if (isOrderGreaterThanZero(metroStop->getStopName(), node->getStopName())) {
        node->setRight(insert(node->getRight(), metroStop));
    } else {
        node->addMetroStop(metroStop);
        return node;
    }
    
    
    int b  = balanceFactor(node);
    if (b>1){
        if ( computeLexiOrder(metroStop->getStopName(), node->getLeft()->getStopName()) < 0)
		    return rotateRight(node);
    }
	if (b<-1){
	if ( computeLexiOrder(metroStop->getStopName(), node->getRight()->getStopName()) > 0)
		return rotateLeft(node);
	}
	if (b>1){
	if ( computeLexiOrder(metroStop->getStopName(), node->getLeft()->getStopName()) > 0)
	{
		node->setLeft(rotateLeft(node->getLeft())) ;
		return rotateRight(node);
	}
	}

	// Right Left Case
	if(b<-1){
	if ( computeLexiOrder(metroStop->getStopName(), node->getRight()->getStopName()) < 0)
	{
		node->setRight(rotateRight(node->getRight())) ;
		return rotateLeft(node);
	}
	}
	
	return node;
}
void AVLTree::inOrderTraversal(AVLNode* node) {
    if (node == nullptr) {
        return;
    }
    inOrderTraversal(node->getLeft());
    cout << node->getStopName() << endl;
    inOrderTraversal(node->getRight());
}

int AVLTree::getTotalNodes(AVLNode* node) {
    if (node == NULL) {
        return 0;
    }
    int totalNodes = 1 + getTotalNodes(node->getLeft()) + getTotalNodes(node->getRight());
    return totalNodes;
}


void AVLTree::populateTree(MetroLine* metroLine) {
    
    MetroStop* travel = NULL;
    travel = metroLine->getNode();
    
    while(travel != NULL){
        
        root = (insert(root, travel));
       
        travel = travel->getNextStop();
       
    }
    
    setRoot(root);
}



AVLNode* AVLTree::searchStop(string stopName) {
    AVLNode* node = this->getRoot();

    while (node != nullptr) {
        int comparisonResult = stringCompare(stopName, node->getStopName());

        if (comparisonResult > 0) {
            node = node->getRight();
        } else if (comparisonResult < 0) {
            node = node->getLeft();
        } else {
            // Return the node if the stop is found
            return node;
        }
    }

    // Return nullptr if the stop is not found
    return nullptr;
}

// Trip class
class Trip {
private:
    MetroStop* node;
    Trip* prev;
    int x;

public:
    Trip(MetroStop* metroStop, Trip* previousTrip);

    // Getter methods
    MetroStop* getNode() const;
    Trip* getPrev() const;
    int getx() const;
    
    void setx(int value){
        x = value;
    }

};

Trip::Trip(MetroStop* metroStop, Trip* previousTrip) {
    node = metroStop;
    prev = previousTrip;
}



MetroStop* Trip::getNode() const {
    return node;
}

Trip* Trip::getPrev() const {
    return prev;
}

int Trip::getx() const {
    return x;
}

// Exploration class is a queue that stores unexplored Trip objects
class Exploration {
private:

    std::queue<Trip*> trips;

public:
    Exploration();

    // Getter methods
    std::queue<Trip*> getTrips() const;

    // Setter methods
    void enqueue(Trip* trip);
    Trip* dequeue();
    bool isEmpty() const;
};

Exploration::Exploration() {
}

std::queue<Trip*> Exploration::getTrips() const {
    return trips;
}

void Exploration::enqueue(Trip* trip) {
    trips.push(trip);
}

Trip* Exploration::dequeue() {
    
    if (trips.size()==0) {
        return nullptr;
    }
    Trip* trip = trips.front();
    trips.pop();
 
    return trip;
}

bool Exploration::isEmpty() const {
    return trips.empty();
}

class Path {
private:
    std::vector<MetroStop*> stops;
    int totalFare;

public:
    Path();

    // Getter methods
    std::vector<MetroStop*> getStops() const;
    int getTotalFare() const;

    // Setter methods
    void addStop(MetroStop* stop);
    void setTotalFare(int fare);

    // helper functions
    void printPath() const;
};

Path::Path() {
    totalFare = 0;
}

std::vector<MetroStop*> Path::getStops() const {
    return stops;
}

int Path::getTotalFare() const {
    return totalFare;
}

void Path::addStop(MetroStop* stop) {
    stops.push_back(stop);
}

void Path::setTotalFare(int fare) {
    totalFare = fare;
}

void Path::printPath() const {
    for (auto stop : stops) {
        cout << stop->getStopName() << endl;
    }
}




Exploration* checkjunction(string stop, Exploration* exp, Trip* prevtrip, AVLNode* root) {
    // Use auto for better readability
    auto stops = root->getStops();

    if (stops.size() > 1) {
        for (auto i = 0; i < stops.size(); ++i) {
            // Maintain consistency in variable naming
            auto currentStop = stops[i];

            // Maintain consistency in function calls
            if (prevtrip->getNode()->getLine()->getLineName() != currentStop->getLine()->getLineName()) {
                // Create trips for both directions
                Trip* tback = new Trip(currentStop->getPrevStop(), prevtrip);
                tback->setx(1);
                Trip* tforwd = new Trip(currentStop->getNextStop(), prevtrip);
                tforwd->setx(2);

                // Maintain consistency in function calls
                exp->enqueue(tback);
                exp->enqueue(tforwd);
            }
        }
    }

    return exp;
}

Path* getPath(MetroStop* stop, Trip* tt, AVLTree* tree) {
    int fare = 0;
    string newline;

    vector<MetroStop*> metrostops;

    Path* finalpath = new Path();
    MetroStop* backtrav = stop;
    MetroStop* backtravtemp = NULL;

    while (tt != NULL) {
        finalpath->addStop(backtrav);
        fare += backtrav->getFare();

        while (backtrav != tt->getNode()) {
            // Use auto to infer the type
            auto direction = tt->getx();

            switch (direction) {
                case 1:  // Forward
                    backtrav = backtrav->getNextStop();
                    break;

                case 2:  // Backward
                    backtrav = backtrav->getPrevStop();
                    break;
            }

            finalpath->addStop(backtrav);
            fare += backtrav->getFare();

            if (backtrav == tt->getNode()) {
                // Use auto to infer the type
                backtravtemp = (direction == 2) ? backtrav->getPrevStop() : backtrav->getNextStop();
            }
        }

        if (tt->getPrev() == nullptr) {
            finalpath->setTotalFare(fare);
            break;
        } else {
            tt = tt->getPrev();
        }

        newline = tt->getNode()->getLine()->getLineName();

        metrostops = tree->searchStop(backtravtemp->getStopName())->getStops();

        for (const auto& metrostop : metrostops) {
            if (metrostop->getLine()->getLineName() == newline) {
                backtrav = metrostop;
                cout << backtrav->getStopName() << " -- jumping line" << endl;
            }
        }
    }

    return finalpath;
}

// PathFinder class
class PathFinder {
private:
    AVLTree* tree;
    std::vector<MetroLine*> lines;

public:
    PathFinder(AVLTree* avlTree, const std::vector<MetroLine*>& metroLines);
    void createAVLTree();
    Path* findPath(std::string origin, std::string destination);

    // Getter methods
    AVLTree* getTree() const;
    const std::vector<MetroLine*>& getLines() const;
};

PathFinder::PathFinder(AVLTree* avlTree, const std::vector<MetroLine*>& metroLines) {
    tree = avlTree;
    lines = metroLines;
}

AVLTree* PathFinder::getTree() const {
    return tree;
}

const std::vector<MetroLine*>& PathFinder::getLines() const {
    return lines;
}

void PathFinder::createAVLTree() {
    for(int i = 0 ; i<lines.size() ; i++){
        tree->populateTree(lines[i]);
    }
}

Path* PathFinder::findPath(std::string origin, std::string destination) {
    int fare = 0;
    auto explr = new Exploration();  // Using auto for cleaner code
    Exploration* tempexplr = nullptr;
    
    auto node = tree->getRoot();
    auto stop1 = tree->searchStop(origin);

    auto stops = stop1->getStops();

    int i = 0;
    while(i < stops.size()){
        auto currStop = stops[i];
        auto t1 = new Trip(currStop->getPrevStop(), nullptr);
        t1->setx(1);
        auto t2 = new Trip(currStop->getNextStop(), nullptr);
        t2->setx(2);
        explr->enqueue(t1);
        explr->enqueue(t2);
        i++;
    }
   
    while (!explr->isEmpty()) {
        auto travtrip = explr->dequeue();
        auto stop = travtrip->getNode();
        
        while (stop != nullptr) {
            // Using switch for better readability
            switch (travtrip->getx()) {
                case 1: {
                    auto temp = tree->searchStop(stop->getStopName());
                    explr = checkjunction(stop->getStopName(), explr, travtrip, temp);
                    
                    if (stop->getStopName() == destination) {
                        auto finalpath = getPath(stop, travtrip, tree);
                        finalpath->addStop(stop1->getStops()[0]);
                        return finalpath;
                    }
                    stop = stop->getPrevStop();
                    break;
                }
                case 2: {
                    auto temp = tree->searchStop(stop->getStopName());
                    explr = checkjunction(stop->getStopName(), explr, travtrip, temp);
                    
                    if (stop->getStopName() == destination) {
                        auto finalpath = getPath(stop, travtrip, tree);
                        finalpath->addStop(stop1->getStops()[0]);
                        return finalpath;
                    }
                    stop = stop->getNextStop();
                    break;
                }
            }
        }
    }
    return nullptr;
}

bool isBackward(const Trip* trip) {
    return trip->getx() == 2;
}

// Helper function to get the next or previous stop based on the direction
MetroStop* getNextOrPrevStop(const MetroStop* stop, bool isBackward) {
    return isBackward ? stop->getPrevStop() : stop->getNextStop();
}

// Helper function to add stops to the final path and update fare
void addStopsAndUpdateFare(Path* finalpath, MetroStop* stop, int& fare) {
    finalpath->addStop(stop);
    fare += stop->getFare();
}

// Helper function to handle different lines during exploration
void handleDifferentLinesDuringExploration(const MetroStop* backtrav, const std::string& newline) {
    // Perform some operation when encountering a different line during exploration
    // This is just a placeholder, and you can replace it with the actual operation.
    // For example, printing a message, updating fare, etc.
    std::cout << backtrav->getStopName() << " -- jumping line to " << newline << std::endl;
}

// Helper function to handle different lines during path finding
void handleDifferentLinesDuringPathFinding(const MetroStop* backtrav, const std::string& newline) {
    // Perform some operation when encountering a different line during path finding
    // This is just a placeholder, and you can replace it with the actual operation.
    // For example, printing a message, updating fare, etc.
    std::cout << backtrav->getStopName() << " -- jumping line to " << newline << std::endl;
}
void AVLTree::printTree(AVLNode* node, int level) {
    if (node != nullptr) {
        printTree(node->getRight(), level + 1);

        for (int i = 0; i < level; ++i) {
            std::cout << "    ";
        }

        std::cout << node->getStopName() << std::endl;

        printTree(node->getLeft(), level + 1);
    }
}

int getHeight(AVLNode* node) {
    if (node == nullptr) {
        return 0;
    }

    int leftHeight = getHeight(node->getLeft());
    int rightHeight = getHeight(node->getRight());

    return std::max(leftHeight, rightHeight) + 1;
}

bool AVLTree::isTreeBalanced(AVLNode* node) {
    if (node == nullptr) {
        return true;
    }

    int leftHeight = getHeight(node->getLeft());
    int rightHeight = getHeight(node->getRight());

    if (std::abs(leftHeight - rightHeight) > 1) {
        return false;
    }

    return isTreeBalanced(node->getLeft()) && isTreeBalanced(node->getRight());
}

void AVLTree::printNodeDetails(AVLNode* node) {
    if (node != nullptr) {
        std::cout << "Stop Name: " << node->getStopName() << std::endl;
        std::cout << "Left Child: " << (node->getLeft() ? node->getLeft()->getStopName() : "nullptr") << std::endl;
        std::cout << "Right Child: " << (node->getRight() ? node->getRight()->getStopName() : "nullptr") << std::endl;
        std::cout << "------------------------" << std::endl;
    }
}
