window.onload = function() {
    var i = 1000;
    var add_btn = document.getElementById('add_btn');

    add_btn.onclick = function(){

        var table = document.getElementById('syslogs');

        var table_tr = document.createElement('div');
        table_tr.setAttribute('class','table_row');    
        table.appendChild(table_tr);
        var cell_1 = document.createElement('div');
        cell_1.setAttribute('class','value border_bottom');

        var input_1 = document.createElement('input');
        input_1.setAttribute('type','text');
        input_1.setAttribute('name','net_syslog_ip_n'+i);
        input_1.setAttribute('size','17');
        input_1.setAttribute('maxlength','15');
        input_1.setAttribute('value','');
        cell_1.appendChild(input_1);

        var cell_2 = document.createElement('div');
        cell_2.setAttribute('class','value border_bottom');
        var input_2 = document.createElement('input');
        input_2.setAttribute('type','text');
        input_2.setAttribute('name','net_syslog_port_n'+i);
        input_2.setAttribute('size','10');
        input_2.setAttribute('maxlength','5');
        input_2.setAttribute('value','514');
        cell_2.appendChild(input_2);

        var cell_3 = document.createElement('div');
        cell_3.setAttribute('class','value border_bottom');
        var input_31 = document.createElement('input');
        input_31.setAttribute('type','checkbox');
        input_31.setAttribute('name','net_syslog_flows_n'+ i);
        input_31.setAttribute('value','1');
        cell_3.appendChild(input_31);
        cell_3.appendChild(document.createTextNode('Flows\n'));

        var input_32 = document.createElement('input');
        input_32.setAttribute('type','checkbox');
        input_32.setAttribute('name','net_syslog_urls_n'+ i);
        input_32.setAttribute('value','1');
        cell_3.appendChild(input_32);
        cell_3.appendChild(document.createTextNode('URLs\n'));

        var input_33 = document.createElement('input');
        input_33.setAttribute('type','checkbox');
        input_33.setAttribute('name','net_syslog_appliance_n'+ i);
        input_33.setAttribute('value','1');
        cell_3.appendChild(input_33);
        cell_3.appendChild(document.createTextNode('Appliance event log\n'));

        var input_34 = document.createElement('input');
        input_34.setAttribute('type','checkbox');
        input_34.setAttribute('name','net_syslog_airMarshal_n'+ i);
        input_34.setAttribute('value','1');
        cell_3.appendChild(input_34);
        cell_3.appendChild(document.createTextNode('Air Marshal events\n'));

        var input_35 = document.createElement('input');
        input_35.setAttribute('type','checkbox');
        input_35.setAttribute('name','net_syslog_wireless_n'+ i);
        input_35.setAttribute('value','1');
        cell_3.appendChild(input_35);
        cell_3.appendChild(document.createTextNode('Wireless event log\n'));

        var input_36 = document.createElement('input');
        input_36.setAttribute('type','checkbox');
        input_36.setAttribute('name','net_syslog_switch_n'+ i);
        input_36.setAttribute('value','1');
        cell_3.appendChild(input_36);
        cell_3.appendChild(document.createTextNode('Switch event log\n'));

        var cell_4 = document.createElement('div');
        cell_4.setAttribute('class','value border_bottom');
        var input_4 = document.createElement('input');
        input_4.setAttribute('type','button');
        input_4.setAttribute('value','キャンセル');
        input_4.setAttribute('onclick','del_btn(this)');
        cell_4.appendChild(input_4);

        table_tr.appendChild(cell_1);
        table_tr.appendChild(cell_2);
        table_tr.appendChild(cell_3);
        table_tr.appendChild(cell_4);


        i += 1;
    }
}


function del_btn(btn) {
    var table_tr = btn.parentNode.parentNode;
    table_tr.remove();
}

