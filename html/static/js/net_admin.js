window.onload = function() {
    var i = 1000;
    var add_btn = document.getElementById('add_btn');

    add_btn.onclick = function(){
        var table = document.getElementById('admin');

        var row = table.insertRow(-1);
        cell_1 = row.insertCell(-1);
        var input_1 = document.createElement('input');
        input_1.setAttribute('type','text');
        input_1.setAttribute('name','net_username_n'+i);
        input_1.setAttribute('value','');
        cell_1.appendChild(input_1);

        cell_2 = row.insertCell(-1);
        var input_2 = document.createElement('input');
        input_2.setAttribute('type','text');
        input_2.setAttribute('name','net_mail_n'+i);
        input_2.setAttribute('value','');
        cell_2.appendChild(input_2);

        cell_3 = row.insertCell(-1);
        var input_3 = document.createElement('input');
        input_3.setAttribute('type','text');
        input_3.setAttribute('name','net_status_n'+ i);
        input_3.setAttribute('value','');
        cell_3.appendChild(input_3);

        cell_4 = row.insertCell(-1);
        var input_41 = document.createElement('select');
        input_41.setAttribute('name','net_access_n'+ i);
        cell_4.appendChild(input_41);

        var input_42 = document.createElement('option');
        input_42.setAttribute('value','full');
        input_42.appendChild(document.createTextNode('full'));
        input_41.appendChild(input_42);

        var input_43 = document.createElement('option');
        input_43.setAttribute('value','read-only');
        input_43.appendChild(document.createTextNode('read-only'));
        input_41.appendChild(input_43);

        var input_44 = document.createElement('option');
        input_44.setAttribute('value','enterprise');
        input_44.appendChild(document.createTextNode('enterprise'));
        input_41.appendChild(input_44);

        var input_45 = document.createElement('option');
        input_45.setAttribute('value','none');
        input_45.setAttribute('selected','selected');
        input_45.appendChild(document.createTextNode('none'));
        input_41.appendChild(input_45);

        cell_5 = row.insertCell(-1);
        var input_5 = document.createElement('input');
        input_5.setAttribute('type','button');
        input_5.setAttribute('value','キャンセル');
        input_5.setAttribute('onclick','del_btn(this)');
        cell_5.appendChild(input_5);

        i += 1;
    }
}


function del_btn(btn) {
    var table_tr = (btn.parentNode).parentNode;
    table_tr.parentNode.deleteRow(table_tr.sectionRowIndex);
}