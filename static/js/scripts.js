// scripts.js

$(function() {
    // Füge hier deine JavaScript-Logik hinzu

    $('#add_filament').on('click', function() {
        // Beispiel: Logik zum Hinzufügen eines neuen Filaments
        var color = prompt('Gib die Farbe des Filaments ein:');
        var weight = prompt('Gib das Gewicht des Filaments in Gramm ein:');
        
        // Hier kannst du eine Funktion aufrufen, um das neue Filament hinzuzufügen
        // Zum Beispiel: addNewFilament(color, weight);
    });
});
