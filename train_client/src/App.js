import React from 'react';
import
{
  Admin,
  Resource,
  ListGuesser,
  EditGuesser
}
from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';
import PostIcon from '@material-ui/icons/Book';
import UserIcon from '@material-ui/icons/Group';

import Dashboard from './Dashboard';
import authProvider from './authProvider';
import dataProvider from './dataProvider';
import
{
  UserList
}
from './users';

import { PostList, PostEdit, PostCreate } from './posts';

// const dataProvider = jsonServerProvider('http://jsonplaceholder.typicode.com');
const App = () => (
  <Admin dashboard={Dashboard} authProvider={authProvider} dataProvider={dataProvider}>
    <Resource name="posts" list={PostList} edit={PostEdit} create={PostCreate} icon={PostIcon} />
    <Resource name="users" list={UserList} icon={UserIcon} />
  </Admin>
);

export default App;