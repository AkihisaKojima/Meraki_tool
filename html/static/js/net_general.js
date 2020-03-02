window.onload = function() {
    var i = 1;
    var add_btn = document.getElementById('add_btn');

    add_btn.onclick = function(){
        var table = document.getElementById('syslogs');

        var row = table.insertRow(-1);
        cell_1 = row.insertCell(-1);
        var input_1 = document.createElement('input');
        input_1.setAttribute('type','text');
        input_1.setAttribute('name','net_syslog_ip_'+i);
        input_1.setAttribute('size','17');
        input_1.setAttribute('maxlength','15');
        input_1.setAttribute('value','');
        cell_1.appendChild(input_1);

        cell_2 = row.insertCell(-1);
        var input_2 = document.createElement('input');
        input_2.setAttribute('type','text');
        input_2.setAttribute('name','net_syslog_port_'+i);
        input_2.setAttribute('size','10');
        input_2.setAttribute('maxlength','5');
        input_2.setAttribute('value','514');
        cell_2.appendChild(input_2);

        cell_3 = row.insertCell(-1);
        var input_31 = document.createElement('input');
        input_31.setAttribute('type','checkbox');
        input_31.setAttribute('name','net_syslog_flows_'+ i);
        input_31.setAttribute('value','1');
        cell_3.appendChild(input_31);
        cell_3.appendChild(document.createTextNode('Flows\n'));

        var input_32 = document.createElement('input');
        input_32.setAttribute('type','checkbox');
        input_32.setAttribute('name','net_syslog_urls_'+ i);
        input_32.setAttribute('value','1');
        cell_3.appendChild(input_32);
        cell_3.appendChild(document.createTextNode('URLs\n'));

        var input_33 = document.createElement('input');
        input_33.setAttribute('type','checkbox');
        input_33.setAttribute('name','net_syslog_appliance_'+ i);
        input_33.setAttribute('value','1');
        cell_3.appendChild(input_33);
        cell_3.appendChild(document.createTextNode('Appliance event log\n'));

        var input_34 = document.createElement('input');
        input_34.setAttribute('type','checkbox');
        input_34.setAttribute('name','net_syslog_airMarshal_'+ i);
        input_34.setAttribute('value','1');
        cell_3.appendChild(input_34);
        cell_3.appendChild(document.createTextNode('Air Marshal events\n'));

        var input_35 = document.createElement('input');
        input_35.setAttribute('type','checkbox');
        input_35.setAttribute('name','net_syslog_wireless_'+ i);
        input_35.setAttribute('value','1');
        cell_3.appendChild(input_35);
        cell_3.appendChild(document.createTextNode('Wireless event log\n'));

        var input_36 = document.createElement('input');
        input_36.setAttribute('type','checkbox');
        input_36.setAttribute('name','net_syslog_switch_'+ i);
        input_36.setAttribute('value','1');
        cell_3.appendChild(input_36);
        cell_3.appendChild(document.createTextNode('Switch event log\n'));

        i += 1;
    }
}
