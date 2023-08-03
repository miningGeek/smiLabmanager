document.addEventListener('DOMContentLoaded', function () {
 intializeBuildingAndRoomFuntionality();
 intializeRoomsAndEqupFuntionality();
 intializeGroupAndProjectFuntionality();
});

function intializeGroupAndProjectFuntionality(){
  var dropdown = document.querySelector('#id_group');

  dropdown.addEventListener('change', function () {
    groupId = this.value;
    console.log('Selected group ID:', groupId);
    var projDataElement = document.getElementById('id_proj_data');
if (projDataElement) {
  // The element exists, do something with it
  projDataElement.disabled = false;
  // ... other code ...
} else {
  // The element doesn't exist, handle the situation
  console.log("Element with ID 'id_proj_data' not found in the HTML.");
}

    if (groupId) {
      document.querySelector('#id_proj_data').disabled = false;
      document.querySelector('#id_proj_data').innerHTML = '<option value="">Loading...</option>';
      fetch(`/get_projects?group_id=${groupId}`)
        .then(response => response.json())
        .then(data => {
          var projectSelect = document.getElementById('id_proj_data');
          while (projectSelect.firstChild) {
            projectSelect.removeChild(projectSelect.firstChild);
          }

          var defaultOption = document.createElement('option');
          defaultOption.value = '';
          defaultOption.textContent = 'Select Project';
          projectSelect.appendChild(defaultOption);

          data.forEach(function (project) {
            var option = document.createElement('option');
            option.value = project.id;
            option.textContent = project.name;
            projectSelect.appendChild(option);
          });
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      document.querySelector('#id_proj_data').disabled = true;
      document.querySelector('#id_proj_data').innerHTML = '<option value="">Select project</option>';

    }
  });
}

function intializeBuildingAndRoomFuntionality(){
  var dropdown = document.querySelector('#id_building');

  dropdown.addEventListener('change', function () {
    buildingId = this.value;
    console.log('Selected building ID:', buildingId);


    if (buildingId) {
      document.querySelector('#id_room').disabled = false;
      document.querySelector('#id_room').innerHTML = '<option value="">Loading...</option>';
      fetch(`/get_rooms?building_id=${buildingId}`)
        .then(response => response.json())
        .then(data => {
          var roomSelect = document.getElementById('id_room');
          while (roomSelect.firstChild) {
            roomSelect.removeChild(roomSelect.firstChild);
          }

          var defaultOption = document.createElement('option');
          defaultOption.value = '';
          defaultOption.textContent = 'Select Room';
          roomSelect.appendChild(defaultOption);

          data.forEach(function (room) {
            var option = document.createElement('option');
            option.value = room.id;
            option.textContent = room.name;
            roomSelect.appendChild(option);
          });
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      document.querySelector('#id_room').disabled = true;
      document.querySelector('#id_room').innerHTML = '<option value="">Select Room</option>';
      document.querySelector('#id_equip_name').disabled = true;
      document.querySelector('#id_equip_name').innerHTML = '<option value="">Select Equipment</option>';
    }
  });
}

function intializeRoomsAndEqupFuntionality(){
  var dropdown = document.querySelector('#id_room');

  dropdown.addEventListener('change', function () {
    roomId = this.value;
    console.log('Selected Room ID:', roomId);

    if (roomId) {
      document.querySelector('#id_equip_name').disabled = false;
      document.querySelector('#id_equip_name').innerHTML = '<option value="">Loading...</option>';
      fetch(`/get_equipments?room_id=${roomId}&building_id=${buildingId}`)
        .then(response => response.json())
        .then(data => {
          var equipSelect = document.getElementById('id_equip_name');
          while (equipSelect.firstChild) {
            equipSelect.removeChild(equipSelect.firstChild);
          }

          var defaultOption = document.createElement('option');
          defaultOption.value = '';
          defaultOption.textContent = 'Select Equip Name';
          equipSelect.appendChild(defaultOption);

          data.forEach(function (equip) {
            var option = document.createElement('option');
            option.value = equip.id;
            option.textContent = equip.name;
            equipSelect.appendChild(option);
          });
        })
        .catch(error => {
          console.log(error);
        });
    } else {
      document.querySelector('#id_equip_name').disabled = true;
      document.querySelector('#id_equip_name').innerHTML = '<option value="">Select Equipment</option>';
    }
  });
}


