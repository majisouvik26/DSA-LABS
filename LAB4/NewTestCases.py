from StudentSolution import TravelDesk,Location,BinarySearchTree,TransportService,Vehicle,Trip
def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    if node is None:
        return True

    node_value = node.get_departure_time()
    
    if node_value <= min_value or node_value >= max_value:
        return False

    return (is_bst(node.get_left_ptr(), min_value, node_value) and
            is_bst(node.get_right_ptr(), node_value, max_value))


def test_add_trip():
    travel_desk = TravelDesk()

    # Add trips
    for i in range(10):
        vehicle_number = "A" + str(i)
        travel_desk.add_trip(vehicle_number, 4, "LocationA", "LocationB", 1000 + i * 100)

    # Add trips for LocationX
    for i in range(10):
        vehicle_number = "X" + str(i)
        travel_desk.add_trip(vehicle_number, 3, "LocationX", "LocationY", 1500 + i * 100)

    # Verify that the tree is a proper BST
    locationA = Location(None)
    locationX = Location(None)
    for i in travel_desk.locations:
        if i.name == "LocationA":
            locationA = i
    for i in travel_desk.locations:
        if i.name == "LocationX":
            locationX = i

    root_location_a = locationA.get_service_ptr("LocationB").get_bst_head()
    assert is_bst(root_location_a)

    root_location_x = locationX.get_service_ptr("LocationY").get_bst_head()
    assert is_bst(root_location_x)

    trips_from_location_a = travel_desk.show_trips("LocationA", 0, 2000)
    trips_from_location_x = travel_desk.show_trips("LocationX", 0, 2000)

    # Assert the number of trips from LocationA and LocationX
    assert len(trips_from_location_a) == 10
    assert len(trips_from_location_x) == 5

def test_book_trip():
    travel_desk = TravelDesk()
    travel_desk.add_trip("XYZ789", 3, "LocationX", "LocationY", 1500)

    booked_trip = travel_desk.book_trip("LocationX", "LocationY", "XYZ789", 1500)
    assert booked_trip is not None
    assert booked_trip.get_booked_seats() == 1

def test_book_trip_max_capacity():
    travel_desk = TravelDesk()
    travel_desk.add_trip("LMN456", 2, "LocationP", "LocationQ", 1200)

    booked_trip = travel_desk.book_trip("LocationP", "LocationQ", "LMN456", 1200)
    assert booked_trip is not None
    assert booked_trip.get_booked_seats() == 1

    second_booking = travel_desk.book_trip("LocationP", "LocationQ", "LMN456", 1200)
    assert  second_booking is not None
    assert second_booking.get_booked_seats() == 2

def test_show_trips_by_time():
    travel_desk = TravelDesk()
    travel_desk.add_trip("ABC123", 4, "LocationA", "LocationB", 1000)
    travel_desk.add_trip("XYZ789", 3, "LocationX", "LocationY", 1500)

    trips = travel_desk.show_trips("LocationA", 800, 1200)
    assert len(trips) == 1

def test_location_name():
    location = Location("LocationC")
    assert location.get_name() == "LocationC"

    location.set_name("NewLocation")
    assert location.get_name() == "NewLocation"

def test_add_trip_to_vehicle():
    vehicle = Vehicle("ABC123", 4)
    trip = Trip(vehicle, "LocationA", "LocationB", 1000)

    vehicle.add_trip(trip)
    trips = vehicle.get_trips()
    assert len(trips) == 1

def test_trip_departure_time():
    vehicle = Vehicle("ABC123", 4)
    trip = Trip(vehicle, "LocationA", "LocationB", 1000)

    trip.set_departure_time(1100)
    assert trip.get_departure_time() == 1100

if __name__ == "__main__":
    # Run the test cases
    test_add_trip()
    test_book_trip()
    test_book_trip_max_capacity()
    test_show_trips_by_time()
    test_location_name()
    test_add_trip_to_vehicle()
    test_trip_departure_time()

    print("All test cases passed.")