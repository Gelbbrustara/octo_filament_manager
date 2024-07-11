// scripts.js
//Version: Beta (C) V 1.1

$(function() {
    // Load initial filaments on page load
    $.ajax({
        url: API_BASEURL + "plugin/filamentmanager",
        type: "GET",
        dataType: "json",
        success: function(response) {
            displayFilaments(response);
        }
    });

    // Function to display filaments
    function displayFilaments(filaments) {
        var filamentList = $("#filament_list");
        filamentList.empty();

        $.each(filaments, function(index, filament) {
            var filamentItem = `
                <div class="filament">
                    <span class="color-circle" style="background-color: ${filament.color};"></span>
                    <span class="name">${filament.name}</span>
                    <div class="usage-bar" style="width: ${filament.usage}%;"></div>
                    <button class="delete-btn" data-name="${filament.name}">Delete</button>
                </div>
            `;
            filamentList.append(filamentItem);
        });
    }

    // Add filament button click event
    $("#add_filament_button").on("click", function() {
        var name = prompt("Enter filament name:");
        var color = prompt("Enter filament color:");
        var usage = prompt("Enter filament usage (in %):");

        var data = {
            name: name,
            color: color,
            usage: parseInt(usage)
        };

        // Add filament via API
        $.ajax({
            url: API_BASEURL + "plugin/filamentmanager",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function(response) {
                displayFilaments(response.filaments);
            }
        });
    });

    // Delete filament button click event
    $("#filament_list").on("click", ".delete-btn", function() {
        var name = $(this).data("name");

        // Delete filament via API
        $.ajax({
            url: API_BASEURL + "plugin/filamentmanager",
            type: "DELETE",
            contentType: "application/json",
            data: JSON.stringify({name: name}),
            success: function(response) {
                displayFilaments(response.filaments);
            }
        });
    });
});
