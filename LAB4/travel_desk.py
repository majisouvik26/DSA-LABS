class Vehicle:
    def __init__(self, vehicle_number, seating_capacity):
        self.vehicle_number = vehicle_number
        self.seating_capacity = seating_capacity
        self.trips = []

    def get_vehicle_number(self):
        return self.vehicle_number

    def set_vehicle_number(self, new_vehicle_number):
        self.vehicle_number = new_vehicle_number

    def get_seating_capacity(self):
        return self.seating_capacity

    def set_seating_capacity(self, new_seating_capacity):
        self.seating_capacity = new_seating_capacity

    def get_trips(self):
        return self.trips

    def add_trip(self, trip):
        self.trips.append(trip)

class Trip:
    def __init__(self, vehicle, pick_up_location, drop_location, departure_time):
        self.vehicle = vehicle
        self.pick_up_location = pick_up_location
        self.drop_location = drop_location
        self.departure_time = departure_time
        self.booked_seats = 0

    def get_vehicle(self):
        return self.vehicle

    def get_pick_up_location(self):
        return self.pick_up_location

    def set_pick_up_location(self, new_pick_up_location):
        self.pick_up_location = new_pick_up_location

    def get_drop_location(self):
        return self.drop_location

    def set_drop_location(self, new_drop_location):
        self.drop_location = new_drop_location

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_booked_seats(self):
        return self.booked_seats

    def set_booked_seats(self, new_booked_seats):
        self.booked_seats = new_booked_seats

class Location:
    def __init__(self, name, service_ptr=None):
        
        self.service_ptrs =  []
        self.trips = []
        self.name = name
        
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_service_ptr(self, drop_location):
        for service in self.service_ptrs:
            if drop_location == service.get_name():
                return service
        return None

    def set_service_ptr(self, drop_location):
        service = TransportService(drop_location)
        self.service_ptrs.append(service)

    def add_trip(self, trip):
        if trip.get_pick_up_location() == self.name:
            self.trips.append(trip)

    def get_service_ptrs(self):
        return self.service_ptrs

class BinaryTreeNode:
    def __init__(self, departure_time=0, trip_node_ptr=None, parent_ptr=None):
        self.left_ptr = None
        self.right_ptr = None
        self.parent_ptr = parent_ptr
        self.departure_time = departure_time
        self.trip_node_ptr = trip_node_ptr

    def get_left_ptr(self):
        return self.left_ptr

    def set_left_ptr(self, new_left_ptr):
        self.left_ptr = new_left_ptr

    def get_right_ptr(self):
        return self.right_ptr

    def set_right_ptr(self, new_right_ptr):
        self.right_ptr = new_right_ptr

    def get_parent_ptr(self):
        return self.parent_ptr

    def set_parent_ptr(self, new_parent_ptr):
        self.parent_ptr = new_parent_ptr

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def get_trip_node_ptr(self):
        return self.trip_node_ptr

    def set_trip_node_ptr(self, new_trip_node_ptr):
        self.trip_node_ptr = new_trip_node_ptr

class BinaryTree:
    def __init__(self):
        self.root = None

    
    def get_height(self):
        # Return the height of the tree (not implemented here)
        def height(root):
            if root is None:
                return 0;
            return 1 + max(height(root.get_left_ptr()),height(root.get_right_ptr()))
        return height(self.root)
    def get_number_of_nodes(self):
        def num_of_nodes(root):
            if root is None:
                return 0
            return 1 + num_of_nodes(root.get_left_ptr()) + num_of_nodes(root.get_right_ptr())
        return num_of_nodes(self.root)

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def element_with_minimum_key(self, temp):
        while temp.get_left_ptr():
            temp = temp.get_left_ptr()
        return temp

    def element_with_maximum_key(self, temp):
        while temp.get_right_ptr():
            temp = temp.get_right_ptr()
        return temp

    def get_element_with_minimum_key(self):
        return self.element_with_minimum_key(self.root)

    def get_element_with_maximum_key(self):
        return self.element_with_maximum_key(self.root)

    def inorder_traversal(self, root, result):
        if root is None:
            return
        self.inorder_traversal(root.get_left_ptr(), result)
        result.append(root)
        self.inorder_traversal(root.get_right_ptr(), result)

    def delete_data(self, root, d):
        if not root:
            return None
        if root.get_departure_time() == d:
            if not root.get_left_ptr() and not root.get_right_ptr():
                del root
                return None
            if root.get_left_ptr() and not root.get_right_ptr():
                temp = root.get_left_ptr()
                del root
                return temp
            if not root.get_left_ptr() and root.get_right_ptr():
                temp = root.get_right_ptr()
                del root
                return temp
            if root.get_left_ptr() and root.get_right_ptr():
                n = self.max_node(root.get_left_ptr())
                root.set_departure_time(n)
                root.set_left_ptr(self.delete_data(root.get_left_ptr(), n))
        else:
            if root.get_departure_time() > d:
                root.set_left_ptr(self.delete_data(root.get_left_ptr(), d))
            else:
                root.set_right_ptr(self.delete_data(root.get_right_ptr(), d))

    def search_node_with_key(self, key):
        current = self.root
        while current and current.get_departure_time() != key:
            if key < current.get_departure_time():
                current = current.get_left_ptr()
            else:
                current = current.get_right_ptr()
        return current

    def find_successor(self, root, key):
        successor = None
        while root:
            if key < root.get_departure_time():
                successor = root
                root = root.get_left_ptr()
            elif key > root.get_departure_time():
                root = root.get_right_ptr()
            else:
                if root.get_right_ptr():
                    temp = root.get_right_ptr()
                    while temp.get_left_ptr():
                        temp = temp.get_left_ptr()
                    successor = temp
                break
        return successor

    def find_predecessor(self, root, key):
        predecessor = None
        while root:
            if key < root.get_departure_time():
                root = root.get_left_ptr()
            elif key > root.get_departure_time():
                predecessor = root
                root = root.get_right_ptr()
            else:
                if root.get_left_ptr():
                    temp = root.get_left_ptr()
                    while temp.get_right_ptr():
                        temp = temp.get_right_ptr()
                    predecessor = temp
                break
        return predecessor

    def get_successor_node(self, node):
        result = self.find_successor(self.root, node.get_departure_time())
        return result

    def get_predecessor_node(self, node):
        result = self.find_predecessor(self.root, node.get_departure_time())
        return result
        
    
class TransportService:
    def __init__(self, name, location_ptr=None, bst_head=None):
        self.name = name
        self.location_ptr = location_ptr
        self.bst_head = bst_head

    def get_name(self):
        return self.name

    def get_location_ptr(self):
        return self.location_ptr

    def set_location_ptr(self, new_location_ptr):
        self.location_ptr = new_location_ptr

    def get_bst_head(self):
        return self.bst_head

    def set_bst_head(self, new_bst_head):
        self.bst_head = new_bst_head
    '''
    def add_trip(self, key, trip):
        new_node = BinaryTreeNode(key, trip)
        if not self.bst_head:
            self.set_bst_head(new_node)
        else:
            temp = self.bst_head
            parent = None
            while temp:
                parent = temp
                if key > temp.get_departure_time():
                    temp = temp.get_right_ptr()
                else:
                    temp = temp.get_left_ptr()
            if parent is None:
                self.set_bst_head(new_node)
            elif key > parent.get_departure_time():
                parent.set_right_ptr(new_node)
            else:
                parent.set_left_ptr(new_node)'''
  
    def add_trip(self, key, trip):
        # Add the trip to the BST (not implemented here)
        souvik = self.bst_head
        parent = None
        for sayan in range(45):
            pass
        new_node = BinaryTreeNode(key,trip)
        while souvik is not None:
            parent = souvik
            if key > souvik.get_departure_time():
                souvik = souvik.get_right_ptr()
            else:
                souvik = souvik.get_left_ptr()
        if parent is None:
            self.set_bst_head(new_node)
        
        elif key > parent.get_departure_time():
            parent.set_right_ptr(new_node)
            
        else:
            parent.set_left_ptr(new_node)
    
class TravelDesk:
    def __init__(self):
        self.vehicles = []
        self.locations = []
    
    def inorder_traversal_with_time_range(self, root, after_time, before_time, result):
        if root is None:
            return

        if after_time <= root.get_departure_time() <= before_time:
            self.inorder_traversal_with_time_range(root.get_left_ptr(), after_time, before_time, result)
            result.append(root)
            self.inorder_traversal_with_time_range(root.get_right_ptr(), after_time, before_time, result)
        elif root.get_departure_time() < after_time:
            self.inorder_traversal_with_time_range(root.get_right_ptr(), after_time, before_time, result)
           
        else:
            self.inorder_traversal_with_time_range(root.get_left_ptr(), after_time, before_time, result)
            
    def get_location(self, location):
        for loc in self.locations:
            if loc.get_name() == location:
                return loc
        return None
    
    def add_location(self, pick_up_location, drop_location, trip):
        location_found = False
        for loc in self.locations:
            if loc.get_name() == pick_up_location:
                location_found = True
                loc.add_trip(trip)
                if not loc.get_service_ptr(drop_location):
                    loc.set_service_ptr(drop_location)
                loc.get_service_ptr(drop_location).add_trip(trip.get_departure_time(), trip)
                break

        if not location_found:
            loc = Location(pick_up_location)
            loc.set_service_ptr(drop_location)
            loc.add_trip(trip)
            loc.get_service_ptr(drop_location).add_trip(trip.get_departure_time(), trip)
            self.locations.append(loc)

    def add_trip(self, vehicle_number, seating_capacity, pick_up_location, drop_location, departure_time):
        vehicle = None
        for v in self.vehicles:
            if v.get_vehicle_number() == vehicle_number:
                vehicle = v
                break
        if vehicle is None:
            vehicle = Vehicle(vehicle_number,seating_capacity)
            self.vehicles.append(vehicle)
        for i in range(5):
            pass
        trip = Trip(vehicle,pick_up_location,drop_location,departure_time)
        vehicle.add_trip(trip)
       
        self.add_location(pick_up_location,drop_location,trip)
            
    def show_trips(self, pick_up_location, after_time, before_time):
        flag = []
        result = []
        object = self.get_location(pick_up_location)

        if after_time > before_time:
            after_time, before_time = before_time, after_time

        if object is not None:
            serv = object.get_service_ptrs()

            for s in serv:
                self.inorder_traversal(s.get_bst_head(), flag)

            for f in flag:
                if after_time <= f.get_departure_time() < before_time:
                    result.append(f.get_trip_node_ptr())

        return result
        
    def inorder_traversal(self, root, result):
        if root is None:
            return
        self.inorder_traversal(root.get_left_ptr(), result)
        result.append(root)
        self.inorder_traversal(root.get_right_ptr(), result)
        

    
    
        
    def book_trip(self, pick_up_location, drop_location, vehicle_number, departure_time):
        # Find the corresponding trip to book the seat and have proper validation 
        trip = None
        object = None
        for v in self.vehicles:
            if v.get_vehicle_number() == vehicle_number:
                object = v
                break
        if not object:
            return None
        trips = object.get_trips()
        for t in trips:
            if t.get_pick_up_location() == pick_up_location and t.get_drop_location() == drop_location:
                trip = t
                break
        if not trip:
            return None
            
        if trip.get_booked_seats() < object.get_seating_capacity():
            trip.set_booked_seats(trip.get_booked_seats() + 1)
      
            return trip
            
        #if all seats are booked 
        if trip.get_booked_seats() == object.get_seating_capacity():
            loc = self.get_location(pick_up_location)
            serv = loc.get_service_ptr(drop_location)
            serv.get_bst_head().delete_data(departure_time)
            
            for i in range(len(object.get_trips())):
                if object.get_trips()[i].get_pick_up_location() == pick_up_location and object.get_trips()[i].get_drop_location() == drop_location and object.get_trips()[i].get_departure_time() == departure_time:
                    object.get_trips().pop(i)
                    break
            for i in range(len(loc.get_trips())):
                if loc.get_trips()[i].get_pick_up_location() == pick_up_location and loc.get_trips()[i].get_drop_location() == drop_location and loc.get_trips()[i].get_departure_time() == departure_time:
                    loc.get_trips().pop(i)
                    break   
                
        return None
    
    def show_tripsbydestination(self, pick_up_location, destination, after_time, before_time):
        flag = []
        result = []
        object = self.get_location(pick_up_location)

        if after_time > before_time:
            after_time, before_time = before_time, after_time

        if object is not None:
            serv = object.get_service_ptrs()

            for s in serv:
                if s.get_name() == destination:
                     self.inorder_traversal_with_time_range(s.get_bst_head(), after_time, before_time, flag)

            for f in flag:
                result.append(f.get_trip_node_ptr())

        return result
        
