import '../Setting/App.css';
import React, { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom";
import axios, { Axios } from "axios";
import { Layout, Select, Row, Col, Space, Divider, PageHeader, Menu, icon, Typography, Result, Button } from "antd";
import Room_list from '../Room/Room_list.js';
import Carousel from '../Home/Carousel';
import {
    HomeOutlined,
    ShopOutlined,
    WalletOutlined,
    LoginOutlined,
    LogoutOutlined,
    MailOutlined,
    PhoneOutlined,
    IdcardOutlined,
    createFromIconfontCN,
} from '@ant-design/icons';
import {
    Router,
    BrowserRouter,
    Routes,
    Route,
    Link
} from "react-router-dom";

const { Header, Content, Footer } = Layout;
const { Title } = Typography;
const IconFont = createFromIconfontCN({
    scriptUrl: '//at.alicdn.com/t/font_8d5l8fzk5b87iudi.js',
});

const change_payment_status_URL = "http://localhost:8000/hotelPortal/change_payment_status";

function App() {
    const onClick = () => {
        window.location.href = '/';
    }

    const [searchParams] = useSearchParams();

    useEffect(() => {
        let paymentId = searchParams.get('payment_id')
        axios.post(change_payment_status_URL, {
            data: {
                paymentId: paymentId,
            }
        }, {
            withCredentials: true,
            headers: {
                'X-CSRFToken': window.sessionStorage.getItem('CSRF-Token')
            }
        }).then((res) => {
            // deal with the response.

        }).catch((err) => {
            if (err.response.status == 403) {
                window.location.href = 'hotelPortal/#/403';
            } else if (err.response.status == 404) {
                window.location.href = 'hotelPortal/#/404';
            } else if (err.response.status == 500) {
                window.location.href = 'hotelPortal/#/500';
            }
        })
    }, [])

    return (
        <Layout className="layout">
            <Header>
                <div className="logo" />
                <Menu
                    theme="dark"
                    mode="horizontal"
                    // defaultSelectedKeys={['1']}
                    items={[
                        { key: 1, label: (<Link to='/home'>home</Link>), icon: <HomeOutlined /> },
                        { key: 2, label: (<Link to='/room_list'>room list</Link>), icon: <ShopOutlined /> },
                        { key: 3, label: (<Link to='/order_list'>order list</Link>), icon: <WalletOutlined /> },
                        { key: 4, label: (<Link to='/login'>login</Link>), icon: <LoginOutlined /> },
                        { key: 5, label: (<Link to='/register'>register</Link>), icon: <LogoutOutlined /> }
                    ]}
                />
            </Header>

            <Content style={{ padding: '0 50px', }}>

                <Result
                    status="success"
                    title="Successfully Checkout The Order!"
                    subTitle="Welcome to our hotel!"
                    extra={[
                        <Button type="primary" onClick={onClick}>
                            Go Home Page
                        </Button>,
                        // <Button key="buy">Buy Again</Button>,
                    ]}
                />

            </Content>
            <Footer
                style={{ textAlign: 'center' }}
            >

                Final Project Team 8
            </Footer>
        </Layout>
    );
}

export default App;