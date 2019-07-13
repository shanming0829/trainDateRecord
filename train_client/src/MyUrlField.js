/**
 * 
 * @authors Shanming (shanming0428@163.com)
 * @date    2019-07-12 23:34:19
 * @version $Id$
 */

import React from 'react';
import { withStyles } from '@material-ui/core/styles';
import LaunchIcon from '@material-ui/icons/Launch';

const MyUrlStyles = {
    link: {
        textDecoration: 'none',
    },
    icon: {
        width: '0.5em',
        paddingLeft: 2,
    }
}

const MyUrlField = (
{
    record = {},
    source,
    classes
}) => (
    <a href={record[source]} className={classes.link}>
        {record[source]}
        <LaunchIcon className={classes.icon}/>
    </a>
)

export default withStyles(MyUrlStyles)(MyUrlField);
